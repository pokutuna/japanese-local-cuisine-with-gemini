from _typeshed import Incomplete
from collections.abc import Generator
from scrapy.http import Request as Request

logger: Incomplete

class DepthMiddleware:
    maxdepth: Incomplete
    stats: Incomplete
    verbose_stats: Incomplete
    prio: Incomplete
    def __init__(self, maxdepth, stats, verbose_stats: bool = False, prio: int = 1) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    def process_spider_output(self, response, result, spider): ...
    async def process_spider_output_async(self, response, result, spider) -> Generator[Incomplete, None, None]: ...
