from _typeshed import Incomplete
from scrapy import signals as signals
from scrapy.exceptions import ScrapyDeprecationWarning as ScrapyDeprecationWarning
from scrapy.utils.httpobj import urlparse_cached as urlparse_cached
from scrapy.utils.url import url_is_from_any_domain as url_is_from_any_domain

class HttpAuthMiddleware:
    @classmethod
    def from_crawler(cls, crawler): ...
    auth: Incomplete
    domain_unset: bool
    domain: Incomplete
    def spider_opened(self, spider) -> None: ...
    def process_request(self, request, spider) -> None: ...
