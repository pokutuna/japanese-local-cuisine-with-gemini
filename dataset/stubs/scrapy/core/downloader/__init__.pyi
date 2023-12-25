from _typeshed import Incomplete
from scrapy import Request as Request, Spider as Spider, signals as signals
from scrapy.core.downloader.handlers import DownloadHandlers as DownloadHandlers
from scrapy.core.downloader.middleware import DownloaderMiddlewareManager as DownloaderMiddlewareManager
from scrapy.crawler import Crawler as Crawler
from scrapy.http import Response as Response
from scrapy.resolver import dnscache as dnscache
from scrapy.settings import BaseSettings as BaseSettings
from scrapy.signalmanager import SignalManager as SignalManager
from scrapy.utils.defer import mustbe_deferred as mustbe_deferred
from scrapy.utils.httpobj import urlparse_cached as urlparse_cached
from twisted.internet.defer import Deferred

class Slot:
    concurrency: Incomplete
    delay: Incomplete
    randomize_delay: Incomplete
    active: Incomplete
    queue: Incomplete
    transferring: Incomplete
    lastseen: int
    latercall: Incomplete
    def __init__(self, concurrency: int, delay: float, randomize_delay: bool) -> None: ...
    def free_transfer_slots(self) -> int: ...
    def download_delay(self) -> float: ...
    def close(self) -> None: ...

class Downloader:
    DOWNLOAD_SLOT: str
    settings: Incomplete
    signals: Incomplete
    slots: Incomplete
    active: Incomplete
    handlers: Incomplete
    total_concurrency: Incomplete
    domain_concurrency: Incomplete
    ip_concurrency: Incomplete
    randomize_delay: Incomplete
    middleware: Incomplete
    per_slot_settings: Incomplete
    def __init__(self, crawler: Crawler) -> None: ...
    def fetch(self, request: Request, spider: Spider) -> Deferred: ...
    def needs_backout(self) -> bool: ...
    def close(self) -> None: ...
