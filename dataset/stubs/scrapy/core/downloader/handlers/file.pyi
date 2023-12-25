from scrapy.responsetypes import responsetypes as responsetypes
from scrapy.utils.decorators import defers as defers

class FileDownloadHandler:
    lazy: bool
    def download_request(self, request, spider): ...
