from _typeshed import Incomplete
from scrapy.crawler import Crawler as Crawler
from scrapy.exceptions import NotConfigured as NotConfigured
from scrapy.settings import Settings as Settings
from scrapy.utils.conf import build_component_list as build_component_list
from scrapy.utils.misc import create_instance as create_instance, load_object as load_object

logger: Incomplete

class AddonManager:
    crawler: Incomplete
    addons: Incomplete
    def __init__(self, crawler: Crawler) -> None: ...
    def load_settings(self, settings: Settings) -> None: ...
