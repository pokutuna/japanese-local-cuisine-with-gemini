from _typeshed import Incomplete
from scrapy.core.downloader.handlers.http import HTTPDownloadHandler as HTTPDownloadHandler
from scrapy.exceptions import NotConfigured as NotConfigured
from scrapy.utils.boto import is_botocore_available as is_botocore_available
from scrapy.utils.httpobj import urlparse_cached as urlparse_cached
from scrapy.utils.misc import create_instance as create_instance

class S3DownloadHandler:
    anon: Incomplete
    def __init__(self, settings, *, crawler: Incomplete | None = None, aws_access_key_id: Incomplete | None = None, aws_secret_access_key: Incomplete | None = None, aws_session_token: Incomplete | None = None, httpdownloadhandler=..., **kw) -> None: ...
    @classmethod
    def from_crawler(cls, crawler, **kwargs): ...
    def download_request(self, request, spider): ...
