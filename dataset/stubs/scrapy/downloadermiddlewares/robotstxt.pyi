from _typeshed import Incomplete
from scrapy.exceptions import IgnoreRequest as IgnoreRequest, NotConfigured as NotConfigured
from scrapy.http import Request as Request
from scrapy.http.request import NO_CALLBACK as NO_CALLBACK
from scrapy.utils.httpobj import urlparse_cached as urlparse_cached
from scrapy.utils.log import failure_to_exc_info as failure_to_exc_info
from scrapy.utils.misc import load_object as load_object

logger: Incomplete

class RobotsTxtMiddleware:
    DOWNLOAD_PRIORITY: int
    crawler: Incomplete
    def __init__(self, crawler) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    def process_request(self, request, spider): ...
    def process_request_2(self, rp, request, spider) -> None: ...
    def robot_parser(self, request, spider): ...
