from _typeshed import Incomplete
from scrapy import Request as Request
from scrapy.spiderloader import SpiderLoader as SpiderLoader
from scrapy.spiders import Spider as Spider
from scrapy.utils.defer import deferred_from_coro as deferred_from_coro
from scrapy.utils.misc import arg_to_iter as arg_to_iter
from twisted.internet.defer import Deferred as Deferred
from types import CoroutineType, ModuleType
from typing import Any, AsyncGenerator, Generator, Iterable, Literal, Optional, Type, overload

logger: Incomplete

@overload
def iterate_spider_output(result: AsyncGenerator) -> AsyncGenerator: ...
@overload
def iterate_spider_output(result: CoroutineType) -> Deferred: ...
@overload
def iterate_spider_output(result: _T) -> Iterable: ...
def iter_spider_classes(module: ModuleType) -> Generator[Type[Spider], Any, None]: ...
@overload
def spidercls_for_request(spider_loader: SpiderLoader, request: Request, default_spidercls: Type[Spider], log_none: bool = ..., log_multiple: bool = ...) -> Type[Spider]: ...
@overload
def spidercls_for_request(spider_loader: SpiderLoader, request: Request, default_spidercls: Literal[None], log_none: bool = ..., log_multiple: bool = ...) -> Optional[Type[Spider]]: ...
@overload
def spidercls_for_request(spider_loader: SpiderLoader, request: Request, *, log_none: bool = ..., log_multiple: bool = ...) -> Optional[Type[Spider]]: ...

class DefaultSpider(Spider):
    name: str
