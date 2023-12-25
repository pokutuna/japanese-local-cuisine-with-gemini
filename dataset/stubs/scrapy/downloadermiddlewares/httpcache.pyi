from _typeshed import Incomplete
from scrapy import signals as signals
from scrapy.crawler import Crawler as Crawler
from scrapy.exceptions import IgnoreRequest as IgnoreRequest, NotConfigured as NotConfigured
from scrapy.http.request import Request as Request
from scrapy.http.response import Response as Response
from scrapy.settings import Settings as Settings
from scrapy.spiders import Spider as Spider
from scrapy.statscollectors import StatsCollector as StatsCollector
from scrapy.utils.misc import load_object as load_object
from typing import Optional, TypeVar

HttpCacheMiddlewareTV = TypeVar('HttpCacheMiddlewareTV', bound='HttpCacheMiddleware')

class HttpCacheMiddleware:
    DOWNLOAD_EXCEPTIONS: Incomplete
    policy: Incomplete
    storage: Incomplete
    ignore_missing: Incomplete
    stats: Incomplete
    def __init__(self, settings: Settings, stats: StatsCollector) -> None: ...
    @classmethod
    def from_crawler(cls, crawler: Crawler) -> HttpCacheMiddlewareTV: ...
    def spider_opened(self, spider: Spider) -> None: ...
    def spider_closed(self, spider: Spider) -> None: ...
    def process_request(self, request: Request, spider: Spider) -> Optional[Response]: ...
    def process_response(self, request: Request, response: Response, spider: Spider) -> Response: ...
    def process_exception(self, request: Request, exception: Exception, spider: Spider) -> Optional[Response]: ...
