from _typeshed import Incomplete
from scrapy.exceptions import NotConfigured as NotConfigured
from scrapy.http import Response as Response, TextResponse as TextResponse
from scrapy.responsetypes import responsetypes as responsetypes
from scrapy.utils.deprecate import ScrapyDeprecationWarning as ScrapyDeprecationWarning
from scrapy.utils.gz import gunzip as gunzip

ACCEPTED_ENCODINGS: Incomplete

class HttpCompressionMiddleware:
    stats: Incomplete
    def __init__(self, stats: Incomplete | None = None) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    def process_request(self, request, spider) -> None: ...
    def process_response(self, request, response, spider): ...
