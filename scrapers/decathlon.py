import logging
from .base import BaseScraper

log = logging.getLogger(__name__)

# Decathlon Belgium runs on the VTEX platform, which exposes a public search API.
SEARCH_URL = "https://www.decathlon.be/api/catalog_system/pub/products/search"


class DecathlonScraper(BaseScraper):
    name = "decathlon"

    def search(self, query: str, max_results: int = 3) -> list[dict]:
        resp = self._get(
            SEARCH_URL,
            params={"fq": f"ft:{query}", "_from": 0, "_to": max_results - 1},
            extra_headers={"Accept": "application/json"},
        )
        products = resp.json()
        results = []

        for p in products:
            try:
                offer = p["items"][0]["sellers"][0]["commertialOffer"]
                price = float(offer["Price"])
                if price <= 0:
                    continue
                in_stock = int(offer.get("AvailableQuantity", 0)) > 0
                slug = p.get("linkText", "")
                results.append({
                    "name":     p["productName"],
                    "price":    price,
                    "currency": "EUR",
                    "url":      f"https://www.decathlon.be/{slug}/p",
                    "in_stock": in_stock,
                })
            except (KeyError, IndexError, TypeError, ValueError):
                continue

        return results[:max_results]
