from _typeshed import Incomplete
from scrapy.spiders import Spider as Spider
from scrapy.utils.spider import iterate_spider_output as iterate_spider_output

class InitSpider(Spider):
    def start_requests(self): ...
    def initialized(self, response: Incomplete | None = None): ...
    def init_request(self): ...
