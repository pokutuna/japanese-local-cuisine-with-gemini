import scrapy
from scrapy.http.response import Response as Response
from scrapy.utils.decorators import deprecated as deprecated
from scrapy.utils.python import to_bytes as to_bytes, to_unicode as to_unicode
from typing import Any, Callable, Iterable, Tuple, Union

def get_base_url(response: scrapy.http.response.text.TextResponse) -> str: ...
def get_meta_refresh(response: scrapy.http.response.text.TextResponse, ignore_tags: Iterable[str] = ('script', 'noscript')) -> Union[Tuple[None, None], Tuple[float, str]]: ...
def response_status_message(status: Union[bytes, float, int, str]) -> str: ...
def response_httprepr(response: Response) -> bytes: ...
def open_in_browser(response: Union['scrapy.http.response.html.HtmlResponse', 'scrapy.http.response.text.TextResponse'], _openfunc: Callable[[str], Any] = ...) -> Any: ...
