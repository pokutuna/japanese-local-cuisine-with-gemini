from _typeshed import Incomplete
from logging import Logger
from scrapy.exceptions import NotConfigured as NotConfigured, ScrapyDeprecationWarning as ScrapyDeprecationWarning
from scrapy.http.request import Request as Request
from scrapy.settings import Settings as Settings
from scrapy.spiders import Spider as Spider
from scrapy.utils.misc import load_object as load_object
from scrapy.utils.python import global_object_name as global_object_name
from scrapy.utils.response import response_status_message as response_status_message
from typing import Optional, Type, Union

retry_logger: Incomplete

def backwards_compatibility_getattr(self, name): ...

class BackwardsCompatibilityMetaclass(type):
    __getattr__ = backwards_compatibility_getattr

def get_retry_request(request: Request, *, spider: Spider, reason: Union[str, Exception, Type[Exception]] = 'unspecified', max_retry_times: Optional[int] = None, priority_adjust: Optional[int] = None, logger: Logger = ..., stats_base_key: str = 'retry'): ...

class RetryMiddleware(metaclass=BackwardsCompatibilityMetaclass):
    max_retry_times: Incomplete
    retry_http_codes: Incomplete
    priority_adjust: Incomplete
    exceptions_to_retry: Incomplete
    def __init__(self, settings) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    def process_response(self, request, response, spider): ...
    def process_exception(self, request, exception, spider): ...
    __getattr__ = backwards_compatibility_getattr
