import logging
from _typeshed import Incomplete
from scrapy import signals as signals
from scrapy.crawler import Crawler as Crawler
from scrapy.http import Request as Request, Response as Response
from scrapy.settings import BaseSettings as BaseSettings
from scrapy.spiders.crawl import CrawlSpider as CrawlSpider, Rule as Rule
from scrapy.spiders.feed import CSVFeedSpider as CSVFeedSpider, XMLFeedSpider as XMLFeedSpider
from scrapy.spiders.sitemap import SitemapSpider as SitemapSpider
from scrapy.utils.trackref import object_ref as object_ref
from scrapy.utils.url import url_is_from_spider as url_is_from_spider
from twisted.internet.defer import Deferred
from typing import Any, Iterable, Optional, Union
from typing_extensions import Self

class Spider(object_ref):
    name: str
    custom_settings: Optional[dict]
    start_urls: Incomplete
    def __init__(self, name: Optional[str] = None, **kwargs: Any) -> None: ...
    @property
    def logger(self) -> logging.LoggerAdapter: ...
    def log(self, message: Any, level: int = ..., **kw: Any) -> None: ...
    @classmethod
    def from_crawler(cls, crawler: Crawler, *args: Any, **kwargs: Any) -> Self: ...
    def start_requests(self) -> Iterable[Request]: ...
    def parse(self, response: Response, **kwargs: Any) -> Any: ...
    @classmethod
    def update_settings(cls, settings: BaseSettings) -> None: ...
    @classmethod
    def handles_request(cls, request: Request) -> bool: ...
    @staticmethod
    def close(spider: Spider, reason: str) -> Union[Deferred, None]: ...
