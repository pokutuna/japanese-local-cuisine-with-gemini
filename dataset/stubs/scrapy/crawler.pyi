from _typeshed import Incomplete
from scrapy import Spider as Spider, signals as signals
from scrapy.addons import AddonManager as AddonManager
from scrapy.core.engine import ExecutionEngine as ExecutionEngine
from scrapy.exceptions import ScrapyDeprecationWarning as ScrapyDeprecationWarning
from scrapy.extension import ExtensionManager as ExtensionManager
from scrapy.interfaces import ISpiderLoader as ISpiderLoader
from scrapy.logformatter import LogFormatter as LogFormatter
from scrapy.settings import BaseSettings as BaseSettings, Settings as Settings, overridden_settings as overridden_settings
from scrapy.signalmanager import SignalManager as SignalManager
from scrapy.statscollectors import StatsCollector as StatsCollector
from scrapy.utils.log import LogCounterHandler as LogCounterHandler, configure_logging as configure_logging, get_scrapy_root_handler as get_scrapy_root_handler, install_scrapy_root_handler as install_scrapy_root_handler, log_reactor_info as log_reactor_info, log_scrapy_info as log_scrapy_info
from scrapy.utils.misc import create_instance as create_instance, load_object as load_object
from scrapy.utils.ossignal import install_shutdown_handlers as install_shutdown_handlers, signal_names as signal_names
from scrapy.utils.reactor import install_reactor as install_reactor, is_asyncio_reactor_installed as is_asyncio_reactor_installed, verify_installed_asyncio_event_loop as verify_installed_asyncio_event_loop, verify_installed_reactor as verify_installed_reactor
from scrapy.utils.request import RequestFingerprinter as RequestFingerprinter
from twisted.internet.defer import Deferred as Deferred
from typing import Any, Dict, Generator, Type, Union

logger: Incomplete

class Crawler:
    spidercls: Incomplete
    settings: Incomplete
    addons: Incomplete
    signals: Incomplete
    crawling: bool
    extensions: Incomplete
    stats: Incomplete
    logformatter: Incomplete
    request_fingerprinter: Incomplete
    spider: Incomplete
    engine: Incomplete
    def __init__(self, spidercls: Type[Spider], settings: Union[None, Dict[str, Any], Settings] = None, init_reactor: bool = False) -> None: ...
    def crawl(self, *args: Any, **kwargs: Any) -> Generator[Deferred, Any, None]: ...
    def stop(self) -> Generator[Deferred, Any, None]: ...

class CrawlerRunner:
    crawlers: Incomplete
    settings: Incomplete
    spider_loader: Incomplete
    bootstrap_failed: bool
    def __init__(self, settings: Union[Dict[str, Any], Settings, None] = None) -> None: ...
    def crawl(self, crawler_or_spidercls: Union[Type[Spider], str, Crawler], *args: Any, **kwargs: Any) -> Deferred: ...
    def create_crawler(self, crawler_or_spidercls: Union[Type[Spider], str, Crawler]) -> Crawler: ...
    def stop(self) -> Deferred: ...
    def join(self) -> Generator[Deferred, Any, None]: ...

class CrawlerProcess(CrawlerRunner):
    def __init__(self, settings: Union[Dict[str, Any], Settings, None] = None, install_root_handler: bool = True) -> None: ...
    def start(self, stop_after_crawl: bool = True, install_signal_handlers: bool = True) -> None: ...
