from _typeshed import Incomplete
from scrapy import signals as signals
from scrapy.exceptions import NotConfigured as NotConfigured
from scrapy.utils.trackref import live_refs as live_refs

class MemoryDebugger:
    stats: Incomplete
    def __init__(self, stats) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    def spider_closed(self, spider, reason) -> None: ...
