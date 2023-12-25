from scrapy.core.downloader.contextfactory import load_context_factory_from_settings as load_context_factory_from_settings
from scrapy.core.http2.agent import H2Agent as H2Agent, H2ConnectionPool as H2ConnectionPool, ScrapyProxyH2Agent as ScrapyProxyH2Agent
from scrapy.crawler import Crawler as Crawler
from scrapy.http import Request as Request, Response as Response
from scrapy.settings import Settings as Settings
from scrapy.spiders import Spider as Spider
from scrapy.utils.python import to_bytes as to_bytes
from twisted.internet.base import DelayedCall as DelayedCall
from twisted.internet.defer import Deferred as Deferred
from typing import Optional, TypeVar

H2DownloadHandlerOrSubclass = TypeVar('H2DownloadHandlerOrSubclass', bound='H2DownloadHandler')

class H2DownloadHandler:
    def __init__(self, settings: Settings, crawler: Optional[Crawler] = None) -> None: ...
    @classmethod
    def from_crawler(cls, crawler: Crawler) -> H2DownloadHandlerOrSubclass: ...
    def download_request(self, request: Request, spider: Spider) -> Deferred: ...
    def close(self) -> None: ...

class ScrapyH2Agent:
    def __init__(self, context_factory, pool: H2ConnectionPool, connect_timeout: int = 10, bind_address: Optional[bytes] = None, crawler: Optional[Crawler] = None) -> None: ...
    def download_request(self, request: Request, spider: Spider) -> Deferred: ...
