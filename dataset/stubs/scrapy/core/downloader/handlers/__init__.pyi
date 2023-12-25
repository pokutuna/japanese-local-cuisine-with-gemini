from _typeshed import Incomplete
from scrapy import Request as Request, Spider as Spider, signals as signals
from scrapy.crawler import Crawler as Crawler
from scrapy.exceptions import NotConfigured as NotConfigured, NotSupported as NotSupported
from scrapy.utils.httpobj import urlparse_cached as urlparse_cached
from scrapy.utils.misc import create_instance as create_instance, load_object as load_object
from scrapy.utils.python import without_none_values as without_none_values
from twisted.internet.defer import Deferred

logger: Incomplete

class DownloadHandlers:
    def __init__(self, crawler: Crawler) -> None: ...
    def download_request(self, request: Request, spider: Spider) -> Deferred: ...
