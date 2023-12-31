from scrapy.exceptions import ScrapyDeprecationWarning as ScrapyDeprecationWarning
from twisted.internet.defer import Deferred as Deferred
from typing import Any, Callable

def deprecated(use_instead: Any = None) -> Callable: ...
def defers(func: Callable) -> Callable[..., Deferred]: ...
def inthread(func: Callable) -> Callable[..., Deferred]: ...
