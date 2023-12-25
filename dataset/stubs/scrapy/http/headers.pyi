from _typeshed import Incomplete
from scrapy.utils.datatypes import CaseInsensitiveDict as CaseInsensitiveDict, CaselessDict as CaselessDict
from scrapy.utils.python import to_unicode as to_unicode

class Headers(CaselessDict):
    encoding: Incomplete
    def __init__(self, seq: Incomplete | None = None, encoding: str = 'utf-8') -> None: ...
    def update(self, seq) -> None: ...
    def normkey(self, key): ...
    def normvalue(self, value): ...
    def __getitem__(self, key): ...
    def get(self, key, def_val: Incomplete | None = None): ...
    def getlist(self, key, def_val: Incomplete | None = None): ...
    def setlist(self, key, list_) -> None: ...
    def setlistdefault(self, key, default_list=()): ...
    def appendlist(self, key, value) -> None: ...
    def items(self): ...
    def values(self): ...
    def to_string(self): ...
    def to_unicode_dict(self): ...
    def __copy__(self): ...
    copy = __copy__
