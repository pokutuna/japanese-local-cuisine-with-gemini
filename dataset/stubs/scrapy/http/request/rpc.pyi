from _typeshed import Incomplete
from scrapy.http.request import Request as Request
from scrapy.utils.python import get_func_args as get_func_args
from typing import Optional

DUMPS_ARGS: Incomplete

class XmlRpcRequest(Request):
    def __init__(self, *args, encoding: Optional[str] = None, **kwargs) -> None: ...
