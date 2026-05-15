import sqlite3
import logging
from datetime import datetime, timedelta
from contextlib import contextmanager

log = logging.getLogger(__name__)


class Database:
    def __init__(self, path: str):
        self.path = path

    @contextmanager
    def _conn(self):
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()

    def init(self):
        with self._conn() as conn:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS prices (
                    id           INTEGER PRIMARY KEY AUTOINCREMENT,
                    item_id      TEXT    NOT NULL,
                    retailer     TEXT    NOT NULL,
                    product_name TEXT    NOT NULL,
                    price        REAL    NOT NULL,
                    currency     TEXT    NOT NULL DEFAULT 'EUR',
                    url          TEXT,
                    in_stock     INTEGER NOT NULL DEFAULT 1,
                    recorded_at  TEXT    NOT NULL
                );
                CREATE INDEX IF NOT EXISTS idx_prices_item_retailer
                    ON prices (item_id, retailer, recorded_at);
            """)
        log.info("Database initialised at %s", self.path)

    def record_price(self, *, item_id, retailer, product_name, price,
                     url=None, currency="EUR", in_stock=True):
        with self._conn() as conn:
            conn.execute(
                """INSERT INTO prices
                       (item_id, retailer, product_name, price, currency, url, in_stock, recorded_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (item_id, retailer, product_name, price, currency,
                 url, int(in_stock), datetime.utcnow().isoformat()),
            )

    def get_latest_prices(self, item_id: str) -> list[dict]:
        """Most recent price per (retailer, product_name)."""
        with self._conn() as conn:
            rows = conn.execute(
                """SELECT retailer, product_name, price, currency, url, in_stock, MAX(recorded_at) AS recorded_at
                   FROM prices
                   WHERE item_id = ?
                   GROUP BY retailer, product_name
                   ORDER BY price ASC""",
                (item_id,),
            ).fetchall()
        return [dict(r) for r in rows]

    def get_price_history(self, item_id: str, retailer: str, days: int = 30) -> list[dict]:
        cutoff = (datetime.utcnow() - timedelta(days=days)).isoformat()
        with self._conn() as conn:
            rows = conn.execute(
                """SELECT price, recorded_at
                   FROM prices
                   WHERE item_id = ? AND retailer = ? AND recorded_at >= ?
                   ORDER BY recorded_at ASC""",
                (item_id, retailer, cutoff),
            ).fetchall()
        return [dict(r) for r in rows]

    def get_stats(self, item_id: str, retailer: str) -> dict | None:
        """Returns avg/min price over 30 days for discount calculation."""
        history = self.get_price_history(item_id, retailer, days=30)
        if not history:
            return None
        prices = [r["price"] for r in history]
        return {
            "avg":   sum(prices) / len(prices),
            "min":   min(prices),
            "max":   max(prices),
            "count": len(prices),
        }

    def get_all_time_low(self, item_id: str, retailer: str) -> float | None:
        with self._conn() as conn:
            row = conn.execute(
                "SELECT MIN(price) FROM prices WHERE item_id = ? AND retailer = ?",
                (item_id, retailer),
            ).fetchone()
        return row[0] if row and row[0] is not None else None
