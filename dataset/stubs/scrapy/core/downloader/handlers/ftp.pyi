from _typeshed import Incomplete
from scrapy.http import Response as Response
from scrapy.responsetypes import responsetypes as responsetypes
from scrapy.utils.httpobj import urlparse_cached as urlparse_cached
from scrapy.utils.python import to_bytes as to_bytes
from twisted.internet.protocol import Protocol

class ReceivedDataProtocol(Protocol):
    body: Incomplete
    size: int
    def __init__(self, filename: Incomplete | None = None) -> None: ...
    def dataReceived(self, data) -> None: ...
    @property
    def filename(self): ...
    def close(self) -> None: ...

class FTPDownloadHandler:
    lazy: bool
    CODE_MAPPING: Incomplete
    default_user: Incomplete
    default_password: Incomplete
    passive_mode: Incomplete
    def __init__(self, settings) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    def download_request(self, request, spider): ...
    client: Incomplete
    def gotClient(self, client, request, filepath): ...
