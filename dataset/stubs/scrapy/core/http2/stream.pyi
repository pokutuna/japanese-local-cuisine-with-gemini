from _typeshed import Incomplete
from enum import Enum
from h2.exceptions import H2Error
from hpack import HeaderTuple as HeaderTuple
from scrapy.core.http2.protocol import H2ClientProtocol as H2ClientProtocol
from scrapy.http import Request as Request
from scrapy.http.headers import Headers as Headers
from scrapy.responsetypes import responsetypes as responsetypes
from twisted.internet.defer import Deferred
from twisted.internet.error import ConnectionClosed
from typing import List, Optional

logger: Incomplete

class InactiveStreamClosed(ConnectionClosed):
    request: Incomplete
    def __init__(self, request: Request) -> None: ...

class InvalidHostname(H2Error):
    request: Incomplete
    expected_hostname: Incomplete
    expected_netloc: Incomplete
    def __init__(self, request: Request, expected_hostname: str, expected_netloc: str) -> None: ...

class StreamCloseReason(Enum):
    ENDED: int
    RESET: int
    CONNECTION_LOST: int
    MAXSIZE_EXCEEDED: int
    CANCELLED: int
    INACTIVE: int
    INVALID_HOSTNAME: int

class Stream:
    stream_id: Incomplete
    metadata: Incomplete
    def __init__(self, stream_id: int, request: Request, protocol: H2ClientProtocol, download_maxsize: int = 0, download_warnsize: int = 0) -> None: ...
    def get_response(self) -> Deferred: ...
    def check_request_url(self) -> bool: ...
    def initiate_request(self) -> None: ...
    def send_data(self) -> None: ...
    def receive_window_update(self) -> None: ...
    def receive_data(self, data: bytes, flow_controlled_length: int) -> None: ...
    def receive_headers(self, headers: List[HeaderTuple]) -> None: ...
    def reset_stream(self, reason: StreamCloseReason = ...) -> None: ...
    def close(self, reason: StreamCloseReason, errors: Optional[List[BaseException]] = None, from_protocol: bool = False) -> None: ...
