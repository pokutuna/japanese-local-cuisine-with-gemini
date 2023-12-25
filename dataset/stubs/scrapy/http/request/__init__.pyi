import scrapy
from _typeshed import Incomplete
from scrapy.http.common import obsolete_setter as obsolete_setter
from scrapy.http.headers import Headers as Headers
from scrapy.utils.curl import curl_to_request_kwargs as curl_to_request_kwargs
from scrapy.utils.python import to_bytes as to_bytes
from scrapy.utils.trackref import object_ref as object_ref
from scrapy.utils.url import escape_ajax as escape_ajax
from typing import Callable, List, Optional, Tuple, TypeVar, Union

RequestTypeVar = TypeVar('RequestTypeVar', bound='Request')

def NO_CALLBACK(*args, **kwargs) -> None: ...

class Request(object_ref):
    attributes: Tuple[str, ...]
    method: Incomplete
    priority: Incomplete
    callback: Incomplete
    errback: Incomplete
    cookies: Incomplete
    headers: Incomplete
    dont_filter: Incomplete
    flags: Incomplete
    def __init__(self, url: str, callback: Optional[Callable] = None, method: str = 'GET', headers: Optional[dict] = None, body: Optional[Union[bytes, str]] = None, cookies: Optional[Union[dict, List[dict]]] = None, meta: Optional[dict] = None, encoding: str = 'utf-8', priority: int = 0, dont_filter: bool = False, errback: Optional[Callable] = None, flags: Optional[List[str]] = None, cb_kwargs: Optional[dict] = None) -> None: ...
    @property
    def cb_kwargs(self) -> dict: ...
    @property
    def meta(self) -> dict: ...
    url: Incomplete
    body: Incomplete
    @property
    def encoding(self) -> str: ...
    def copy(self) -> Request: ...
    def replace(self, *args, **kwargs) -> Request: ...
    @classmethod
    def from_curl(cls, curl_command: str, ignore_unknown_options: bool = True, **kwargs) -> RequestTypeVar: ...
    def to_dict(self, *, spider: Optional['scrapy.Spider'] = None) -> dict: ...
