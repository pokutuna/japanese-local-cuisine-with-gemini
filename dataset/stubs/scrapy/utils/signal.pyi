from _typeshed import Incomplete
from scrapy.exceptions import StopDownload as StopDownload
from scrapy.utils.defer import maybeDeferred_coro as maybeDeferred_coro
from scrapy.utils.log import failure_to_exc_info as failure_to_exc_info
from twisted.internet.defer import Deferred
from typing import Any as TypingAny, List, Tuple

logger: Incomplete

def send_catch_log(signal: TypingAny = ..., sender: TypingAny = ..., *arguments: TypingAny, **named: TypingAny) -> List[Tuple[TypingAny, TypingAny]]: ...
def send_catch_log_deferred(signal: TypingAny = ..., sender: TypingAny = ..., *arguments: TypingAny, **named: TypingAny) -> Deferred: ...
def disconnect_all(signal: TypingAny = ..., sender: TypingAny = ...) -> None: ...
