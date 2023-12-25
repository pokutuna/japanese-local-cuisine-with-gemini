from _typeshed import Incomplete
from scrapy.utils.misc import create_instance as create_instance, load_object as load_object
from scrapy.utils.python import to_unicode as to_unicode

class HTTP10DownloadHandler:
    lazy: bool
    HTTPClientFactory: Incomplete
    ClientContextFactory: Incomplete
    def __init__(self, settings, crawler: Incomplete | None = None) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    def download_request(self, request, spider): ...
