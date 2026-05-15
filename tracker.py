#!/usr/bin/env python3
"""Daily price tracker for NZ van life packing list.
Run manually or via GitHub Actions (see .github/workflows/daily.yml).
"""
import logging
import sys
from datetime import date

import config
from database import Database
from items import ITEMS
from notifier import build_html_report, send_email
from scrapers import ALL_SCRAPERS

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-7s  %(name)s — %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("tracker")

GOOD_DEAL_PCT  = config.GOOD_DEAL_PCT
GREAT_DEAL_PCT = config.GREAT_DEAL_PCT
MAX_RESULTS    = config.MAX_RESULTS_PER_RETAILER


def classify_deal(price: float, stats: dict | None, all_time_low: float | None) -> str | None:
    if all_time_low and price <= all_time_low:
        return "all_time_low"
    if stats and stats["count"] >= 3:
        disc = (stats["avg"] - price) / stats["avg"] * 100
        if disc >= GREAT_DEAL_PCT:
            return "great"
        if disc >= GOOD_DEAL_PCT:
            return "good"
        if disc >= 8:
            return "watch"
    return None


def run():
    db = Database(config.DB_PATH)
    db.init()

    # ── Scrape ──────────────────────────────────────────────────────────────
    total_scraped = 0
    for item in ITEMS:
        retailers = item.get("retailers", {})
        for retailer_key, query in retailers.items():
            scraper = ALL_SCRAPERS.get(retailer_key)
            if not scraper:
                log.warning("No scraper registered for %r", retailer_key)
                continue
            log.info("[%s] %s → %r", item["id"], retailer_key, query)
            results = scraper.safe_search(query, max_results=MAX_RESULTS)
            for r in results:
                db.record_price(
                    item_id=item["id"],
                    retailer=retailer_key,
                    product_name=r["name"],
                    price=r["price"],
                    url=r.get("url", ""),
                    currency=r.get("currency", "EUR"),
                    in_stock=r.get("in_stock", True),
                )
                total_scraped += 1

    log.info("Scraped %d prices", total_scraped)

    # ── Analyse & build report data ─────────────────────────────────────────
    all_prices: dict = {}   # item_id → list of enriched rows
    deals: list     = []

    for item in ITEMS:
        latest = db.get_latest_prices(item["id"])
        if not latest:
            all_prices[item["id"]] = []
            continue

        enriched = []
        for row in latest:
            stats       = db.get_stats(item["id"], row["retailer"])
            atl         = db.get_all_time_low(item["id"], row["retailer"])
            deal_type   = classify_deal(row["price"], stats, atl)
            disc_pct    = 0.0
            if stats and stats["count"] >= 3:
                disc_pct = (stats["avg"] - row["price"]) / stats["avg"] * 100

            enriched_row = {
                **row,
                "item_meta":    item,
                "stats":        stats,
                "deal_type":    deal_type,
                "discount_pct": disc_pct,
            }
            enriched.append(enriched_row)

            if deal_type in ("all_time_low", "great", "good"):
                deals.append(enriched_row)

        # Keep only cheapest per retailer for the full table
        best_per_retailer: dict[str, dict] = {}
        for row in enriched:
            key = row["retailer"]
            if key not in best_per_retailer or row["price"] < best_per_retailer[key]["price"]:
                best_per_retailer[key] = row
        all_prices[item["id"]] = sorted(best_per_retailer.values(), key=lambda x: x["price"])

    # Sort deals: all_time_low first, then by discount %
    deals.sort(key=lambda x: (-{"all_time_low": 3, "great": 2, "good": 1}.get(x["deal_type"], 0),
                               -x["discount_pct"]))

    # ── Email ───────────────────────────────────────────────────────────────
    run_date   = date.today().strftime("%B %-d, %Y")
    deal_count = len(deals)
    subject    = (
        f"🇳🇿 NZ Packing — {deal_count} deal{'s' if deal_count != 1 else ''} found today · {run_date}"
        if deal_count else
        f"🇳🇿 NZ Packing — Daily price update · {run_date}"
    )

    html = build_html_report(deals=deals, all_prices=all_prices, run_date=run_date)

    send_email(
        html_body=html,
        subject=subject,
        email_from=config.EMAIL_FROM,
        email_to=config.EMAIL_TO,
        smtp_host=config.SMTP_HOST,
        smtp_port=config.SMTP_PORT,
        smtp_password=config.SMTP_PASSWORD,
    )

    log.info("Done. %d deals found today.", deal_count)
    return 0


if __name__ == "__main__":
    sys.exit(run())
