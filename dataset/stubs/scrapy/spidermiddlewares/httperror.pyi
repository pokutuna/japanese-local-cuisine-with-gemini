from _typeshed import Incomplete
from scrapy.exceptions import IgnoreRequest as IgnoreRequest

logger: Incomplete

class HttpError(IgnoreRequest):
    response: Incomplete
    def __init__(self, response, *args, **kwargs) -> None: ...

class HttpErrorMiddleware:
    @classmethod
    def from_crawler(cls, crawler): ...
    handle_httpstatus_all: Incomplete
    handle_httpstatus_list: Incomplete
    def __init__(self, settings) -> None: ...
    def process_spider_input(self, response, spider) -> None: ...
    def process_spider_exception(self, response, exception, spider): ...
