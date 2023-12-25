from _typeshed import Incomplete
from parsel import Selector as _ParselSelector
from scrapy.http import TextResponse
from scrapy.utils.trackref import object_ref
from typing import Any, Optional

__all__ = ['Selector', 'SelectorList']

class SelectorList(_ParselSelector.selectorlist_cls, object_ref): ...

class Selector(_ParselSelector, object_ref):
    selectorlist_cls = SelectorList
    response: Incomplete
    def __init__(self, response: Optional[TextResponse] = None, text: Optional[str] = None, type: Optional[str] = None, root: Optional[Any] = ..., **kwargs: Any) -> None: ...
