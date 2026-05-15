from .amazon import AmazonScraper
from .wiggle import WiggleScraper
from .zalando import ZalandoScraper
from .bol import BolScraper

ALL_SCRAPERS = {
    "amazon":  AmazonScraper(),
    "wiggle":  WiggleScraper(),
    "zalando": ZalandoScraper(),
    "bol":     BolScraper(),
}
