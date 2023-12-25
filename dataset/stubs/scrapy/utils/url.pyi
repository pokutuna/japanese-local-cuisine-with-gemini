from w3lib.url import *
from scrapy import Spider as Spider
from scrapy.utils.python import to_unicode as to_unicode
from typing import Iterable, Optional, Type, Union
from urllib.parse import ParseResult

UrlT = Union[str, bytes, ParseResult]

def url_is_from_any_domain(url: UrlT, domains: Iterable[str]) -> bool: ...
def url_is_from_spider(url: UrlT, spider: Type['Spider']) -> bool: ...
def url_has_any_extension(url: UrlT, extensions: Iterable[str]) -> bool: ...
def parse_url(url: UrlT, encoding: Optional[str] = None) -> ParseResult: ...
def escape_ajax(url: str) -> str: ...
def add_http_if_no_scheme(url: str) -> str: ...
def guess_scheme(url: str) -> str: ...
def strip_url(url: str, strip_credentials: bool = True, strip_default_port: bool = True, origin_only: bool = False, strip_fragment: bool = True) -> str: ...