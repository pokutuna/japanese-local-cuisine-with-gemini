from _typeshed import Incomplete
from collections.abc import Generator
from scrapy.exceptions import NotConfigured as NotConfigured
from scrapy.http import Request as Request

logger: Incomplete

class UrlLengthMiddleware:
    maxlength: Incomplete
    def __init__(self, maxlength) -> None: ...
    @classmethod
    def from_settings(cls, settings): ...
    def process_spider_output(self, response, result, spider): ...
    async def process_spider_output_async(self, response, result, spider) -> Generator[Incomplete, None, None]: ...
