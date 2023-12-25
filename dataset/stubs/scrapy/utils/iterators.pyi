from _typeshed import Incomplete
from lxml._types import SupportsReadClose as SupportsReadClose
from scrapy.http import Response as Response, TextResponse as TextResponse
from scrapy.selector import Selector as Selector
from scrapy.utils.python import re_rsearch as re_rsearch, to_unicode as to_unicode
from typing import Any, Dict, Generator, List, Optional, Union

logger: Incomplete

def xmliter(obj: Union[Response, str, bytes], nodename: str) -> Generator[Selector, Any, None]: ...
def xmliter_lxml(obj: Union[Response, str, bytes], nodename: str, namespace: Optional[str] = None, prefix: str = 'x') -> Generator[Selector, Any, None]: ...

class _StreamReader:
    def __init__(self, obj: Union[Response, str, bytes]) -> None: ...
    def read(self, n: int = 65535) -> bytes: ...

def csviter(obj: Union[Response, str, bytes], delimiter: Optional[str] = None, headers: Optional[List[str]] = None, encoding: Optional[str] = None, quotechar: Optional[str] = None) -> Generator[Dict[str, str], Any, None]: ...
