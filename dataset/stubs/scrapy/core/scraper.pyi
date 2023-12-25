from _typeshed import Incomplete
from scrapy import Spider as Spider, signals as signals
from scrapy.core.spidermw import SpiderMiddlewareManager as SpiderMiddlewareManager
from scrapy.crawler import Crawler as Crawler
from scrapy.exceptions import CloseSpider as CloseSpider, DropItem as DropItem, IgnoreRequest as IgnoreRequest
from scrapy.http import Request as Request, Response as Response
from scrapy.logformatter import LogFormatter as LogFormatter
from scrapy.pipelines import ItemPipelineManager as ItemPipelineManager
from scrapy.signalmanager import SignalManager as SignalManager
from scrapy.utils.defer import aiter_errback as aiter_errback, defer_fail as defer_fail, defer_succeed as defer_succeed, iter_errback as iter_errback, parallel as parallel, parallel_async as parallel_async
from scrapy.utils.log import failure_to_exc_info as failure_to_exc_info, logformatter_adapter as logformatter_adapter
from scrapy.utils.misc import load_object as load_object, warn_on_generator_with_return_value as warn_on_generator_with_return_value
from scrapy.utils.spider import iterate_spider_output as iterate_spider_output
from twisted.internet.defer import Deferred
from twisted.python.failure import Failure
from typing import Any, AsyncIterable, Generator, Iterable, Tuple, Union

QueueTuple = Tuple[Union[Response, Failure], Request, Deferred]
logger: Incomplete

class Slot:
    MIN_RESPONSE_SIZE: int
    max_active_size: Incomplete
    queue: Incomplete
    active: Incomplete
    active_size: int
    itemproc_size: int
    closing: Incomplete
    def __init__(self, max_active_size: int = 5000000) -> None: ...
    def add_response_request(self, result: Union[Response, Failure], request: Request) -> Deferred: ...
    def next_response_request_deferred(self) -> QueueTuple: ...
    def finish_response(self, result: Union[Response, Failure], request: Request) -> None: ...
    def is_idle(self) -> bool: ...
    def needs_backout(self) -> bool: ...

class Scraper:
    slot: Incomplete
    spidermw: Incomplete
    itemproc: Incomplete
    concurrent_items: Incomplete
    crawler: Incomplete
    signals: Incomplete
    logformatter: Incomplete
    def __init__(self, crawler: Crawler) -> None: ...
    def open_spider(self, spider: Spider) -> Generator[Deferred, Any, None]: ...
    def close_spider(self, spider: Spider) -> Deferred: ...
    def is_idle(self) -> bool: ...
    def enqueue_scrape(self, result: Union[Response, Failure], request: Request, spider: Spider) -> Deferred: ...
    def call_spider(self, result: Union[Response, Failure], request: Request, spider: Spider) -> Deferred: ...
    def handle_spider_error(self, _failure: Failure, request: Request, response: Union[Response, Failure], spider: Spider) -> None: ...
    def handle_spider_output(self, result: Union[Iterable, AsyncIterable], request: Request, response: Union[Response, Failure], spider: Spider) -> Deferred: ...
