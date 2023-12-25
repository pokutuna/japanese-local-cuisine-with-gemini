from _typeshed import Incomplete
from scrapy import signals as signals
from scrapy.exceptions import NotConfigured as NotConfigured
from scrapy.utils.serialize import ScrapyJSONEncoder as ScrapyJSONEncoder

logger: Incomplete

class PeriodicLog:
    stats: Incomplete
    interval: Incomplete
    multiplier: Incomplete
    task: Incomplete
    encoder: Incomplete
    ext_stats_enabled: Incomplete
    ext_stats_include: Incomplete
    ext_stats_exclude: Incomplete
    ext_delta_enabled: Incomplete
    ext_delta_include: Incomplete
    ext_delta_exclude: Incomplete
    ext_timing_enabled: Incomplete
    def __init__(self, stats, interval: float = 60.0, ext_stats={}, ext_delta={}, ext_timing_enabled: bool = False) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    time_prev: Incomplete
    delta_prev: Incomplete
    stats_prev: Incomplete
    def spider_opened(self, spider) -> None: ...
    def log(self) -> None: ...
    def log_delta(self): ...
    def log_timing(self): ...
    def log_crawler_stats(self): ...
    def param_allowed(self, stat_name, include, exclude): ...
    def spider_closed(self, spider, reason) -> None: ...
