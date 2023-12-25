import logging
from _typeshed import Incomplete
from scrapy.crawler import Crawler as Crawler
from scrapy.exceptions import ScrapyDeprecationWarning as ScrapyDeprecationWarning
from scrapy.settings import Settings as Settings
from scrapy.utils.versions import scrapy_components_versions as scrapy_components_versions
from twisted.python.failure import Failure
from types import TracebackType
from typing import Any, List, Optional, Tuple, Type, Union

logger: Incomplete

def failure_to_exc_info(failure: Failure) -> Optional[Tuple[Type[BaseException], BaseException, Optional[TracebackType]]]: ...

class TopLevelFormatter(logging.Filter):
    loggers: Incomplete
    def __init__(self, loggers: Optional[List[str]] = None) -> None: ...
    def filter(self, record: logging.LogRecord) -> bool: ...

DEFAULT_LOGGING: Incomplete

def configure_logging(settings: Union[Settings, dict, None] = None, install_root_handler: bool = True) -> None: ...
def install_scrapy_root_handler(settings: Settings) -> None: ...
def get_scrapy_root_handler() -> Optional[logging.Handler]: ...
def log_scrapy_info(settings: Settings) -> None: ...
def log_reactor_info() -> None: ...

class StreamLogger:
    logger: Incomplete
    log_level: Incomplete
    linebuf: str
    def __init__(self, logger: logging.Logger, log_level: int = ...) -> None: ...
    def write(self, buf: str) -> None: ...
    def flush(self) -> None: ...

class LogCounterHandler(logging.Handler):
    crawler: Incomplete
    def __init__(self, crawler: Crawler, *args: Any, **kwargs: Any) -> None: ...
    def emit(self, record: logging.LogRecord) -> None: ...

def logformatter_adapter(logkws: dict) -> Tuple[int, str, dict]: ...