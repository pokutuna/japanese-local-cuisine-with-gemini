from _typeshed import Incomplete
from scrapy import Request as Request, Spider as Spider
from scrapy.http import Response as Response
from scrapy.middleware import MiddlewareManager as MiddlewareManager
from scrapy.settings import BaseSettings as BaseSettings
from scrapy.utils.asyncgen import as_async_generator as as_async_generator, collect_asyncgen as collect_asyncgen
from scrapy.utils.conf import build_component_list as build_component_list
from scrapy.utils.defer import deferred_f_from_coro_f as deferred_f_from_coro_f, deferred_from_coro as deferred_from_coro, maybe_deferred_to_future as maybe_deferred_to_future, mustbe_deferred as mustbe_deferred
from scrapy.utils.python import MutableAsyncChain as MutableAsyncChain, MutableChain as MutableChain
from twisted.internet.defer import Deferred as Deferred
from twisted.python.failure import Failure
from typing import Any, Callable, Iterable, Union

logger: Incomplete
ScrapeFunc = Callable[[Union[Response, Failure], Request, Spider], Any]

class SpiderMiddlewareManager(MiddlewareManager):
    component_name: str
    downgrade_warning_done: bool
    def __init__(self, *middlewares: Any) -> None: ...
    def scrape_response(self, scrape_func: ScrapeFunc, response: Response, request: Request, spider: Spider) -> Deferred: ...
    def process_start_requests(self, start_requests: Iterable[Request], spider: Spider) -> Deferred: ...
