from _typeshed import Incomplete
from scrapy.utils.engine import format_engine_status as format_engine_status
from scrapy.utils.trackref import format_live_refs as format_live_refs

logger: Incomplete

class StackTraceDump:
    crawler: Incomplete
    def __init__(self, crawler: Incomplete | None = None) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    def dump_stacktrace(self, signum, frame) -> None: ...

class Debugger:
    def __init__(self) -> None: ...
