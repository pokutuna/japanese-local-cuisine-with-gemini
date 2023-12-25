from _typeshed import Incomplete
from scrapy.utils.asyncgen import as_async_generator as as_async_generator
from typing import Any, AsyncIterable, AsyncIterator, Callable, Dict, Iterable, Iterator, List, Mapping, Optional, Pattern, Tuple, Union, overload

def flatten(x: Iterable) -> list: ...
def iflatten(x: Iterable) -> Iterable: ...
def is_listlike(x: Any) -> bool: ...
def unique(list_: Iterable, key: Callable[[Any], Any] = ...) -> list: ...
def to_unicode(text: Union[str, bytes], encoding: Optional[str] = None, errors: str = 'strict') -> str: ...
def to_bytes(text: Union[str, bytes], encoding: Optional[str] = None, errors: str = 'strict') -> bytes: ...
def re_rsearch(pattern: Union[str, Pattern], text: str, chunk_size: int = 1024) -> Optional[Tuple[int, int]]: ...
def memoizemethod_noargs(method: Callable) -> Callable: ...
def binary_is_text(data: bytes) -> bool: ...
def get_func_args(func: Callable, stripself: bool = False) -> List[str]: ...
def get_spec(func: Callable) -> Tuple[List[str], Dict[str, Any]]: ...
def equal_attributes(obj1: Any, obj2: Any, attributes: Optional[List[Union[str, Callable]]]) -> bool: ...
@overload
def without_none_values(iterable: Mapping) -> dict: ...
@overload
def without_none_values(iterable: Iterable) -> Iterable: ...
def global_object_name(obj: Any) -> str: ...
def garbage_collect() -> None: ...

class MutableChain(Iterable):
    data: Incomplete
    def __init__(self, *args: Iterable) -> None: ...
    def extend(self, *iterables: Iterable) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __next__(self) -> Any: ...

class MutableAsyncChain(AsyncIterable):
    data: Incomplete
    def __init__(self, *args: Union[Iterable, AsyncIterable]) -> None: ...
    def extend(self, *iterables: Union[Iterable, AsyncIterable]) -> None: ...
    def __aiter__(self) -> AsyncIterator: ...
    async def __anext__(self) -> Any: ...
