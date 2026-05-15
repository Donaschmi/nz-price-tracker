import re
import json
import logging
from bs4 import BeautifulSoup
from .base import BaseScraper

log = logging.getLogger(__name__)

SEARCH_URL = "https://www.wiggle.com/searchresults"


class WiggleScraper(BaseScraper):
    name = "wiggle"

    def search(self, query: str, max_results: int = 3) -> list[dict]:
        resp = self._get(SEARCH_URL, params={"descriptionfilter": query})
        soup = BeautifulSoup(resp.text, "html.parser")
        results = []

        # Wiggle embeds product data in a __NEXT_DATA__ JSON blob
        next_data_tag = soup.find("script", id="__NEXT_DATA__")
        if next_data_tag:
            try:
                data = json.loads(next_data_tag.string)
                products = (
                    data.get("props", {})
                        .get("pageProps", {})
                        .get("initialData", {})
                        .get("products", [])
                )
                for p in products[:max_results]:
                    price = p.get("price", {}).get("current") or p.get("price", {}).get("selling")
                    if not price:
                        continue
                    results.append({
                        "name":     p.get("name", "")[:120],
                        "price":    float(price),
                        "currency": "EUR",
                        "url":      "https://www.wiggle.com" + p.get("url", ""),
                        "in_stock": p.get("inStock", True),
                    })
                return results
            except (json.JSONDecodeError, KeyError):
                pass

        # Fallback: parse HTML product cards
        for card in soup.select("[data-e2e='product-card']"):
            try:
                name_el  = card.select_one("[data-e2e='product-card-title']")
                price_el = card.select_one("[data-e2e='product-card-price']")
                link_el  = card.select_one("a[href]")
                if not name_el or not price_el:
                    continue
                price_text = re.sub(r"[^\d.,]", "", price_el.get_text())
                price = float(price_text.replace(",", "."))
                results.append({
                    "name":     name_el.get_text(strip=True)[:120],
                    "price":    price,
                    "currency": "EUR",
                    "url":      "https://www.wiggle.com" + (link_el["href"] if link_el else ""),
                    "in_stock": True,
                })
                if len(results) >= max_results:
                    break
            except (ValueError, AttributeError):
                continue

        return results
