from _typeshed import Incomplete
from scrapy.exceptions import IgnoreRequest as IgnoreRequest, NotConfigured as NotConfigured
from scrapy.http import HtmlResponse as HtmlResponse
from scrapy.utils.httpobj import urlparse_cached as urlparse_cached
from scrapy.utils.response import get_meta_refresh as get_meta_refresh

logger: Incomplete

class BaseRedirectMiddleware:
    enabled_setting: str
    max_redirect_times: Incomplete
    priority_adjust: Incomplete
    def __init__(self, settings) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...

class RedirectMiddleware(BaseRedirectMiddleware):
    def process_response(self, request, response, spider): ...

class MetaRefreshMiddleware(BaseRedirectMiddleware):
    enabled_setting: str
    def __init__(self, settings) -> None: ...
    def process_response(self, request, response, spider): ...
