from _typeshed import Incomplete
from scrapy.exceptions import NotConfigured as NotConfigured
from scrapy.http import HtmlResponse as HtmlResponse

logger: Incomplete

class AjaxCrawlMiddleware:
    lookup_bytes: Incomplete
    def __init__(self, settings) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    def process_response(self, request, response, spider): ...
