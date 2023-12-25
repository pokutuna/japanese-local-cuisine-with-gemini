from _typeshed import Incomplete
from scrapy import Request as Request, Spider as Spider
from scrapy.crawler import Crawler as Crawler
from scrapy.http import Response as Response
from scrapy.utils.request import referer_str as referer_str
from twisted.python.failure import Failure
from typing import Any, Optional, Union
from typing_extensions import Self

SCRAPEDMSG: Incomplete
DROPPEDMSG: Incomplete
CRAWLEDMSG: str
ITEMERRORMSG: str
SPIDERERRORMSG: str
DOWNLOADERRORMSG_SHORT: str
DOWNLOADERRORMSG_LONG: str

class LogFormatter:
    def crawled(self, request: Request, response: Response, spider: Spider) -> dict: ...
    def scraped(self, item: Any, response: Union[Response, Failure], spider: Spider) -> dict: ...
    def dropped(self, item: Any, exception: BaseException, response: Response, spider: Spider) -> dict: ...
    def item_error(self, item: Any, exception: BaseException, response: Response, spider: Spider) -> dict: ...
    def spider_error(self, failure: Failure, request: Request, response: Union[Response, Failure], spider: Spider) -> dict: ...
    def download_error(self, failure: Failure, request: Request, spider: Spider, errmsg: Optional[str] = None) -> dict: ...
    @classmethod
    def from_crawler(cls, crawler: Crawler) -> Self: ...
