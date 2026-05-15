from .idealo import IdealoScraper
from .amazon import AmazonScraper

ALL_SCRAPERS = {
    "idealo": IdealoScraper(),
    "amazon": AmazonScraper(),
}
