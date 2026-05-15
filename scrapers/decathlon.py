import re
import json
import logging
from bs4 import BeautifulSoup
from .base import BaseScraper

log = logging.getLogger(__name__)

SEARCH_URL = "https://www.decathlon.be/fr/search"


class DecathlonScraper(BaseScraper):
    name = "decathlon"

    def search(self, query: str, max_results: int = 3) -> list[dict]:
        resp = self._get(
            SEARCH_URL,
            params={"Ntt": query},
            extra_headers={"Accept-Language": "fr-BE,fr;q=0.9,en;q=0.8"},
        )
        soup = BeautifulSoup(resp.text, "html.parser")

        # Strategy 1: JSON-LD structured data (Decathlon injects this for SEO)
        results = self._parse_jsonld(soup, max_results)
        if results:
            return results

        # Strategy 2: __NEXT_DATA__ or similar embedded JSON blob
        results = self._parse_script_json(soup, max_results)
        if results:
            return results

        # Strategy 3: HTML product cards
        return self._parse_html_cards(soup, max_results)

    def _parse_jsonld(self, soup, max_results):
        results = []
        for tag in soup.find_all("script", type="application/ld+json"):
            try:
                data = json.loads(tag.string or "")
                entries = data if isinstance(data, list) else [data]
                for entry in entries:
                    # ItemList wrapping individual Products
                    if entry.get("@type") == "ItemList":
                        for el in entry.get("itemListElement", []):
                            r = self._extract_product(el.get("item", el))
                            if r:
                                results.append(r)
                    elif entry.get("@type") == "Product":
                        r = self._extract_product(entry)
                        if r:
                            results.append(r)
                    if len(results) >= max_results:
                        return results[:max_results]
            except (json.JSONDecodeError, TypeError):
                continue
        return results

    def _extract_product(self, p):
        name = p.get("name")
        offers = p.get("offers") or p.get("offer")
        if isinstance(offers, list):
            offers = offers[0]
        if not name or not offers:
            return None
        price = offers.get("price") or offers.get("lowPrice")
        if not price:
            return None
        url = p.get("url") or offers.get("url", "")
        return {
            "name":     str(name)[:120],
            "price":    float(price),
            "currency": offers.get("priceCurrency", "EUR"),
            "url":      url,
            "in_stock": offers.get("availability", "") != "OutOfStock",
        }

    def _parse_script_json(self, soup, max_results):
        for tag in soup.find_all("script"):
            src = tag.string or ""
            if "productName" not in src and "\"price\"" not in src:
                continue
            # Try to extract embedded JSON objects that look like product data
            for match in re.finditer(r'\{[^{}]*"price"[^{}]*\}', src):
                try:
                    obj = json.loads(match.group())
                    name  = obj.get("productName") or obj.get("name")
                    price = obj.get("price") or obj.get("Price")
                    url   = obj.get("url") or obj.get("link", "")
                    if name and price:
                        return [{
                            "name":     str(name)[:120],
                            "price":    float(price),
                            "currency": "EUR",
                            "url":      url,
                            "in_stock": True,
                        }]
                except (json.JSONDecodeError, ValueError):
                    continue
        return []

    def _parse_html_cards(self, soup, max_results):
        results = []
        # Decathlon uses various card patterns across their redesigns
        card_selectors = [
            "[class*='product-card']",
            "[class*='product_card']",
            "[data-testid*='product']",
            "[class*='productCard']",
        ]
        cards = []
        for sel in card_selectors:
            cards = soup.select(sel)
            if cards:
                break

        for card in cards:
            try:
                name_el = (
                    card.select_one("[class*='product-title'], [class*='productTitle']") or
                    card.select_one("h2, h3")
                )
                price_el = (
                    card.select_one("[class*='product-price'], [class*='productPrice']") or
                    card.select_one("[class*='price']")
                )
                link_el = card.select_one("a[href]")
                if not name_el or not price_el:
                    continue
                raw = re.sub(r"[^\d,.]", "", price_el.get_text(strip=True))
                price = float(raw.replace(",", "."))
                href = link_el["href"] if link_el else ""
                if href and not href.startswith("http"):
                    href = "https://www.decathlon.be" + href
                results.append({
                    "name":     name_el.get_text(strip=True)[:120],
                    "price":    price,
                    "currency": "EUR",
                    "url":      href,
                    "in_stock": True,
                })
                if len(results) >= max_results:
                    break
            except (ValueError, AttributeError):
                continue
        return results
