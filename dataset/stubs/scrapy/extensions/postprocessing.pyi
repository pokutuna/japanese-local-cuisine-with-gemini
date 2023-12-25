from _typeshed import Incomplete
from io import IOBase
from scrapy.utils.misc import load_object as load_object
from typing import Any, BinaryIO, Dict, List

class GzipPlugin:
    file: Incomplete
    feed_options: Incomplete
    gzipfile: Incomplete
    def __init__(self, file: BinaryIO, feed_options: Dict[str, Any]) -> None: ...
    def write(self, data: bytes) -> int: ...
    def close(self) -> None: ...

class Bz2Plugin:
    file: Incomplete
    feed_options: Incomplete
    bz2file: Incomplete
    def __init__(self, file: BinaryIO, feed_options: Dict[str, Any]) -> None: ...
    def write(self, data: bytes) -> int: ...
    def close(self) -> None: ...

class LZMAPlugin:
    file: Incomplete
    feed_options: Incomplete
    lzmafile: Incomplete
    def __init__(self, file: BinaryIO, feed_options: Dict[str, Any]) -> None: ...
    def write(self, data: bytes) -> int: ...
    def close(self) -> None: ...

class PostProcessingManager(IOBase):
    plugins: Incomplete
    file: Incomplete
    feed_options: Incomplete
    head_plugin: Incomplete
    def __init__(self, plugins: List[Any], file: BinaryIO, feed_options: Dict[str, Any]) -> None: ...
    def write(self, data: bytes) -> int: ...
    def tell(self) -> int: ...
    def close(self) -> None: ...
    def writable(self) -> bool: ...
