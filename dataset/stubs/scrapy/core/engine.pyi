from _typeshed import Incomplete
from scrapy import signals as signals
from scrapy.core.downloader import Downloader as Downloader
from scrapy.core.scheduler import BaseScheduler as BaseScheduler
from scrapy.core.scraper import Scraper as Scraper
from scrapy.crawler import Crawler as Crawler
from scrapy.exceptions import CloseSpider as CloseSpider, DontCloseSpider as DontCloseSpider
from scrapy.http import Request as Request, Response as Response
from scrapy.logformatter import LogFormatter as LogFormatter
from scrapy.settings import BaseSettings as BaseSettings, Settings as Settings
from scrapy.signalmanager import SignalManager as SignalManager
from scrapy.spiders import Spider as Spider
from scrapy.utils.log import failure_to_exc_info as failure_to_exc_info, logformatter_adapter as logformatter_adapter
from scrapy.utils.misc import create_instance as create_instance, load_object as load_object
from scrapy.utils.reactor import CallLaterOnce as CallLaterOnce
from twisted.internet.defer import Deferred
from typing import Any, Callable, Generator, Iterable

logger: Incomplete

class Slot:
    closing: Incomplete
    inprogress: Incomplete
    start_requests: Incomplete
    close_if_idle: Incomplete
    nextcall: Incomplete
    scheduler: Incomplete
    heartbeat: Incomplete
    def __init__(self, start_requests: Iterable[Request], close_if_idle: bool, nextcall: CallLaterOnce, scheduler: BaseScheduler) -> None: ...
    def add_request(self, request: Request) -> None: ...
    def remove_request(self, request: Request) -> None: ...
    def close(self) -> Deferred: ...

class ExecutionEngine:
    crawler: Incomplete
    settings: Incomplete
    signals: Incomplete
    logformatter: Incomplete
    slot: Incomplete
    spider: Incomplete
    running: bool
    paused: bool
    scheduler_cls: Incomplete
    downloader: Incomplete
    scraper: Incomplete
    start_time: Incomplete
    def __init__(self, crawler: Crawler, spider_closed_callback: Callable) -> None: ...
    def start(self) -> Generator[Deferred, Any, None]: ...
    def stop(self) -> Deferred: ...
    def close(self) -> Deferred: ...
    def pause(self) -> None: ...
    def unpause(self) -> None: ...
    def spider_is_idle(self) -> bool: ...
    def crawl(self, request: Request) -> None: ...
    def download(self, request: Request) -> Deferred: ...
    def open_spider(self, spider: Spider, start_requests: Iterable = (), close_if_idle: bool = True) -> Generator[Deferred, Any, None]: ...
    def close_spider(self, spider: Spider, reason: str = 'cancelled') -> Deferred: ...
