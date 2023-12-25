from _typeshed import Incomplete
from scrapy.exceptions import NotConfigured as NotConfigured
from scrapy.http import Response as Response
from scrapy.http.cookies import CookieJar as CookieJar
from scrapy.utils.httpobj import urlparse_cached as urlparse_cached
from scrapy.utils.python import to_unicode as to_unicode

logger: Incomplete

class CookiesMiddleware:
    jars: Incomplete
    debug: Incomplete
    def __init__(self, debug: bool = False) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    def process_request(self, request, spider) -> None: ...
    def process_response(self, request, response, spider): ...
