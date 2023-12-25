from _typeshed import Incomplete
from scrapy.exceptions import NotConfigured as NotConfigured
from scrapy.utils.httpobj import urlparse_cached as urlparse_cached
from scrapy.utils.python import to_bytes as to_bytes

class HttpProxyMiddleware:
    auth_encoding: Incomplete
    proxies: Incomplete
    def __init__(self, auth_encoding: str = 'latin-1') -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    def process_request(self, request, spider) -> None: ...
