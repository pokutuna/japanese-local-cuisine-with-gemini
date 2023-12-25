from _typeshed import Incomplete
from scrapy import Request as Request
from scrapy.http import Headers as Headers
from scrapy.responsetypes import responsetypes as responsetypes
from scrapy.utils.httpobj import urlparse_cached as urlparse_cached
from scrapy.utils.python import to_bytes as to_bytes, to_unicode as to_unicode
from twisted.internet.protocol import ClientFactory
from twisted.web.http import HTTPClient
from urllib.parse import ParseResult as ParseResult

class ScrapyHTTPPageGetter(HTTPClient):
    delimiter: bytes
    headers: Incomplete
    def connectionMade(self) -> None: ...
    def lineReceived(self, line): ...
    def handleHeader(self, key, value) -> None: ...
    def handleStatus(self, version, status, message) -> None: ...
    def handleEndHeaders(self) -> None: ...
    def connectionLost(self, reason) -> None: ...
    def handleResponse(self, response) -> None: ...
    def timeout(self) -> None: ...

class ScrapyHTTPClientFactory(ClientFactory):
    protocol = ScrapyHTTPPageGetter
    waiting: int
    noisy: bool
    followRedirect: bool
    afterFoundGet: bool
    url: Incomplete
    method: Incomplete
    body: Incomplete
    headers: Incomplete
    response_headers: Incomplete
    timeout: Incomplete
    start_time: Incomplete
    deferred: Incomplete
    def __init__(self, request: Request, timeout: float = 180) -> None: ...
    def buildProtocol(self, addr): ...
    headers_time: Incomplete
    def gotHeaders(self, headers) -> None: ...
    def gotStatus(self, version, status, message) -> None: ...
    def page(self, page) -> None: ...
    def noPage(self, reason) -> None: ...
    def clientConnectionFailed(self, _, reason) -> None: ...