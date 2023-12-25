from _typeshed import Incomplete
from scrapy import signals as signals
from scrapy.exceptions import NotConfigured as NotConfigured

logger: Incomplete

class AutoThrottle:
    crawler: Incomplete
    debug: Incomplete
    target_concurrency: Incomplete
    def __init__(self, crawler) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
