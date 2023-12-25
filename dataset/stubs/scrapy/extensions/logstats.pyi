from _typeshed import Incomplete
from scrapy import signals as signals
from scrapy.exceptions import NotConfigured as NotConfigured

logger: Incomplete

class LogStats:
    stats: Incomplete
    interval: Incomplete
    multiplier: Incomplete
    task: Incomplete
    def __init__(self, stats, interval: float = 60.0) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    pagesprev: int
    itemsprev: int
    def spider_opened(self, spider) -> None: ...
    def log(self, spider) -> None: ...
    def spider_closed(self, spider, reason) -> None: ...
