from _typeshed import Incomplete
from scrapy import Spider as Spider, signals as signals
from scrapy.exceptions import NotConfigured as NotConfigured, ScrapyDeprecationWarning as ScrapyDeprecationWarning
from scrapy.extensions.postprocessing import PostProcessingManager as PostProcessingManager
from scrapy.utils.boto import is_botocore_available as is_botocore_available
from scrapy.utils.conf import feed_complete_default_values_from_settings as feed_complete_default_values_from_settings
from scrapy.utils.defer import maybe_deferred_to_future as maybe_deferred_to_future
from scrapy.utils.deprecate import create_deprecated_class as create_deprecated_class
from scrapy.utils.ftp import ftp_store_file as ftp_store_file
from scrapy.utils.log import failure_to_exc_info as failure_to_exc_info
from scrapy.utils.misc import create_instance as create_instance, load_object as load_object
from scrapy.utils.python import get_func_args as get_func_args, without_none_values as without_none_values
from typing import Any, Dict, IO, Optional, Tuple
from zope.interface import Interface

logger: Incomplete
IS_BOTO3_AVAILABLE: bool

def build_storage(builder, uri, *args, feed_options: Incomplete | None = None, preargs=(), **kwargs): ...

class ItemFilter:
    feed_options: Optional[dict]
    item_classes: Tuple
    def __init__(self, feed_options: Optional[dict]) -> None: ...
    def accepts(self, item: Any) -> bool: ...

class IFeedStorage(Interface):
    def __init__(uri, *, feed_options: Incomplete | None = None) -> None: ...
    def open(spider) -> None: ...
    def store(file) -> None: ...

class BlockingFeedStorage:
    def open(self, spider): ...
    def store(self, file): ...

class StdoutFeedStorage:
    def __init__(self, uri, _stdout: Incomplete | None = None, *, feed_options: Incomplete | None = None) -> None: ...
    def open(self, spider): ...
    def store(self, file) -> None: ...

class FileFeedStorage:
    path: Incomplete
    write_mode: Incomplete
    def __init__(self, uri, *, feed_options: Incomplete | None = None) -> None: ...
    def open(self, spider) -> IO[Any]: ...
    def store(self, file) -> None: ...

class S3FeedStorage(BlockingFeedStorage):
    bucketname: Incomplete
    access_key: Incomplete
    secret_key: Incomplete
    session_token: Incomplete
    keyname: Incomplete
    acl: Incomplete
    endpoint_url: Incomplete
    region_name: Incomplete
    s3_client: Incomplete
    def __init__(self, uri, access_key: Incomplete | None = None, secret_key: Incomplete | None = None, acl: Incomplete | None = None, endpoint_url: Incomplete | None = None, *, feed_options: Incomplete | None = None, session_token: Incomplete | None = None, region_name: Incomplete | None = None) -> None: ...
    @classmethod
    def from_crawler(cls, crawler, uri, *, feed_options: Incomplete | None = None): ...

class GCSFeedStorage(BlockingFeedStorage):
    project_id: Incomplete
    acl: Incomplete
    bucket_name: Incomplete
    blob_name: Incomplete
    def __init__(self, uri, project_id, acl) -> None: ...
    @classmethod
    def from_crawler(cls, crawler, uri): ...

class FTPFeedStorage(BlockingFeedStorage):
    host: Incomplete
    port: Incomplete
    username: Incomplete
    password: Incomplete
    path: Incomplete
    use_active_mode: Incomplete
    overwrite: Incomplete
    def __init__(self, uri: str, use_active_mode: bool = False, *, feed_options: Optional[Dict[str, Any]] = None) -> None: ...
    @classmethod
    def from_crawler(cls, crawler, uri, *, feed_options: Incomplete | None = None): ...

class FeedSlot:
    file: Incomplete
    exporter: Incomplete
    storage: Incomplete
    batch_id: Incomplete
    format: Incomplete
    store_empty: Incomplete
    uri_template: Incomplete
    uri: Incomplete
    filter: Incomplete
    feed_options: Incomplete
    spider: Incomplete
    exporters: Incomplete
    settings: Incomplete
    crawler: Incomplete
    itemcount: int
    def __init__(self, storage, uri, format, store_empty, batch_id, uri_template, filter, feed_options, spider, exporters, settings, crawler) -> None: ...
    def start_exporting(self) -> None: ...
    def finish_exporting(self) -> None: ...

class FeedExporter:
    @classmethod
    def from_crawler(cls, crawler): ...
    crawler: Incomplete
    settings: Incomplete
    feeds: Incomplete
    slots: Incomplete
    filters: Incomplete
    storages: Incomplete
    exporters: Incomplete
    def __init__(self, crawler) -> None: ...
    def open_spider(self, spider) -> None: ...
    async def close_spider(self, spider) -> None: ...
    def item_scraped(self, item, spider) -> None: ...
