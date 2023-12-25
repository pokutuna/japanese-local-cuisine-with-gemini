from _typeshed import Incomplete
from collections.abc import Generator
from scrapy.exceptions import DropItem as DropItem, NotConfigured as NotConfigured, ScrapyDeprecationWarning as ScrapyDeprecationWarning
from scrapy.http import Request as Request
from scrapy.http.request import NO_CALLBACK as NO_CALLBACK
from scrapy.pipelines.files import FileException as FileException, FilesPipeline as FilesPipeline
from scrapy.settings import Settings as Settings
from scrapy.utils.misc import md5sum as md5sum
from scrapy.utils.python import get_func_args as get_func_args, to_bytes as to_bytes

class NoimagesDrop(DropItem):
    def __init__(self, *args, **kwargs) -> None: ...

class ImageException(FileException): ...

class ImagesPipeline(FilesPipeline):
    MEDIA_NAME: str
    MIN_WIDTH: int
    MIN_HEIGHT: int
    EXPIRES: int
    THUMBS: Incomplete
    DEFAULT_IMAGES_URLS_FIELD: str
    DEFAULT_IMAGES_RESULT_FIELD: str
    expires: Incomplete
    IMAGES_RESULT_FIELD: Incomplete
    IMAGES_URLS_FIELD: Incomplete
    images_urls_field: Incomplete
    images_result_field: Incomplete
    min_width: Incomplete
    min_height: Incomplete
    thumbs: Incomplete
    def __init__(self, store_uri, download_func: Incomplete | None = None, settings: Incomplete | None = None) -> None: ...
    @classmethod
    def from_settings(cls, settings): ...
    def file_downloaded(self, response, request, info, *, item: Incomplete | None = None): ...
    def image_downloaded(self, response, request, info, *, item: Incomplete | None = None): ...
    def get_images(self, response, request, info, *, item: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...
    def convert_image(self, image, size: Incomplete | None = None, response_body: Incomplete | None = None): ...
    def get_media_requests(self, item, info): ...
    def item_completed(self, results, item, info): ...
    def file_path(self, request, response: Incomplete | None = None, info: Incomplete | None = None, *, item: Incomplete | None = None): ...
    def thumb_path(self, request, thumb_id, response: Incomplete | None = None, info: Incomplete | None = None, *, item: Incomplete | None = None): ...
