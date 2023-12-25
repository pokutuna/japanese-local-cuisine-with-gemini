from _typeshed import Incomplete
from scrapy.http import Headers as Headers, Response as Response
from scrapy.http.request import Request as Request
from scrapy.responsetypes import responsetypes as responsetypes
from scrapy.spiders import Spider as Spider
from scrapy.utils.httpobj import urlparse_cached as urlparse_cached
from scrapy.utils.project import data_path as data_path
from scrapy.utils.python import to_bytes as to_bytes, to_unicode as to_unicode

logger: Incomplete

class DummyPolicy:
    ignore_schemes: Incomplete
    ignore_http_codes: Incomplete
    def __init__(self, settings) -> None: ...
    def should_cache_request(self, request): ...
    def should_cache_response(self, response, request): ...
    def is_cached_response_fresh(self, cachedresponse, request): ...
    def is_cached_response_valid(self, cachedresponse, response, request): ...

class RFC2616Policy:
    MAXAGE: Incomplete
    always_store: Incomplete
    ignore_schemes: Incomplete
    ignore_response_cache_controls: Incomplete
    def __init__(self, settings) -> None: ...
    def should_cache_request(self, request): ...
    def should_cache_response(self, response, request): ...
    def is_cached_response_fresh(self, cachedresponse, request): ...
    def is_cached_response_valid(self, cachedresponse, response, request): ...

class DbmCacheStorage:
    cachedir: Incomplete
    expiration_secs: Incomplete
    dbmodule: Incomplete
    db: Incomplete
    def __init__(self, settings) -> None: ...
    def open_spider(self, spider: Spider): ...
    def close_spider(self, spider) -> None: ...
    def retrieve_response(self, spider, request): ...
    def store_response(self, spider, request, response) -> None: ...

class FilesystemCacheStorage:
    cachedir: Incomplete
    expiration_secs: Incomplete
    use_gzip: Incomplete
    def __init__(self, settings) -> None: ...
    def open_spider(self, spider: Spider): ...
    def close_spider(self, spider) -> None: ...
    def retrieve_response(self, spider: Spider, request: Request): ...
    def store_response(self, spider: Spider, request: Request, response): ...

def parse_cachecontrol(header): ...
def rfc1123_to_epoch(date_str): ...
