from _typeshed import Incomplete
from twisted.internet.defer import Deferred
from twisted.internet.protocol import ProcessProtocol
from twisted.python.failure import Failure as Failure
from typing import Iterable, Optional

class ProcessTest:
    command: Incomplete
    prefix: Incomplete
    cwd: Incomplete
    def execute(self, args: Iterable[str], check_code: bool = True, settings: Optional[str] = None) -> Deferred: ...

class TestProcessProtocol(ProcessProtocol):
    deferred: Incomplete
    out: bytes
    err: bytes
    exitcode: Incomplete
    def __init__(self) -> None: ...
    def outReceived(self, data: bytes) -> None: ...
    def errReceived(self, data: bytes) -> None: ...
    def processEnded(self, status: Failure) -> None: ...
