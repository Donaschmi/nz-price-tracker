import re
import logging
from bs4 import BeautifulSoup
from .base import BaseScraper

log = logging.getLogger(__name__)

SEARCH_URL = "https://www.bol.com/be/en/s/"


class BolScraper(BaseScraper):
    name = "bol"

    def search(self, query: str, max_results: int = 3) -> list[dict]:
        resp = self._get(
            SEARCH_URL,
            params={"searchtext": query, "sort": "price_asc"},
            extra_headers={"Accept-Language": "en-BE,en;q=0.9"},
        )
        soup = BeautifulSoup(resp.text, "html.parser")
        results = []

        for card in soup.select("[data-test='product-card']"):
            try:
                name_el  = card.select_one("[data-test='product-title']")
                price_el = card.select_one("[data-test='price']") or card.select_one(".promo-price")
                link_el  = card.select_one("a[href*='/p/']")
                if not name_el or not price_el:
                    continue
                price_text = re.sub(r"[^\d,.]", "", price_el.get_text())
                price = float(price_text.replace(",", "."))
                href  = link_el["href"] if link_el else ""
                results.append({
                    "name":     name_el.get_text(strip=True)[:120],
                    "price":    price,
                    "currency": "EUR",
                    "url":      href if href.startswith("http") else "https://www.bol.com" + href,
                    "in_stock": True,
                })
                if len(results) >= max_results:
                    break
            except (ValueError, AttributeError):
                continue

        return results
