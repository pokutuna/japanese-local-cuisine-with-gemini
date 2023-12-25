from _typeshed import Incomplete
from collections.abc import Generator
from scrapy.http import Request as Request, XmlResponse as XmlResponse
from scrapy.spiders import Spider as Spider
from scrapy.utils.gz import gunzip as gunzip, gzip_magic_number as gzip_magic_number
from scrapy.utils.sitemap import Sitemap as Sitemap, sitemap_urls_from_robots as sitemap_urls_from_robots

logger: Incomplete

class SitemapSpider(Spider):
    sitemap_urls: Incomplete
    sitemap_rules: Incomplete
    sitemap_follow: Incomplete
    sitemap_alternate_links: bool
    def __init__(self, *a, **kw) -> None: ...
    def start_requests(self) -> Generator[Incomplete, None, None]: ...
    def sitemap_filter(self, entries) -> Generator[Incomplete, None, None]: ...

def regex(x): ...
def iterloc(it, alt: bool = False) -> Generator[Incomplete, Incomplete, None]: ...
