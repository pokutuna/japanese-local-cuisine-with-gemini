from _typeshed import Incomplete
from scrapy.http import HtmlResponse as HtmlResponse, Request as Request, Response as Response
from scrapy.linkextractors import LinkExtractor as LinkExtractor
from scrapy.spiders import Spider as Spider
from scrapy.utils.asyncgen import collect_asyncgen as collect_asyncgen
from scrapy.utils.spider import iterate_spider_output as iterate_spider_output
from typing import Sequence

class Rule:
    link_extractor: Incomplete
    callback: Incomplete
    errback: Incomplete
    cb_kwargs: Incomplete
    process_links: Incomplete
    process_request: Incomplete
    follow: Incomplete
    def __init__(self, link_extractor: Incomplete | None = None, callback: Incomplete | None = None, cb_kwargs: Incomplete | None = None, follow: Incomplete | None = None, process_links: Incomplete | None = None, process_request: Incomplete | None = None, errback: Incomplete | None = None) -> None: ...

class CrawlSpider(Spider):
    rules: Sequence[Rule]
    def __init__(self, *a, **kw) -> None: ...
    def parse_start_url(self, response, **kwargs): ...
    def process_results(self, response: Response, results: list): ...
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs): ...
