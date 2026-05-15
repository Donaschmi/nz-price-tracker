import re
import logging
from bs4 import BeautifulSoup
from .base import BaseScraper

log = logging.getLogger(__name__)

SEARCH_URL = "https://www.amazon.de/s"


class AmazonScraper(BaseScraper):
    name = "amazon_de"

    def search(self, query: str, max_results: int = 3) -> list[dict]:
        resp = self._get(
            SEARCH_URL,
            params={"k": query, "language": "en_GB"},
            extra_headers={"Accept-Language": "en-GB,en;q=0.9"},
        )
        soup = BeautifulSoup(resp.text, "html.parser")
        results = []

        for card in soup.select('[data-asin]:not([data-asin=""])'):
            asin = card.get("data-asin", "").strip()
            if not asin:
                continue

            name_el   = card.select_one("h2 span")
            price_int = card.select_one(".a-price-whole")
            price_frc = card.select_one(".a-price-fraction")

            if not name_el or not price_int:
                continue

            try:
                # German Amazon uses . as thousands separator and , as decimal
                whole = re.sub(r"[^\d]", "", price_int.get_text())
                frac  = re.sub(r"[^\d]", "", price_frc.get_text()) if price_frc else "00"
                price = float(f"{whole}.{frac[:2]}")
                if price <= 0:
                    continue
            except ValueError:
                continue

            results.append({
                "name":     name_el.get_text(strip=True)[:120],
                "price":    price,
                "currency": "EUR",
                "url":      f"https://www.amazon.de/dp/{asin}",
                "in_stock": True,
            })

            if len(results) >= max_results:
                break

        return results
