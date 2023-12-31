from _typeshed import Incomplete
from scrapy.settings import default_settings as default_settings
from types import ModuleType
from typing import Any, Dict, Iterable, Iterator, List, Mapping, MutableMapping, Optional, Tuple, Union
from typing_extensions import Self

SETTINGS_PRIORITIES: Dict[str, int]

def get_settings_priority(priority: Union[int, str]) -> int: ...

class SettingsAttribute:
    value: Incomplete
    priority: Incomplete
    def __init__(self, value: Any, priority: int) -> None: ...
    def set(self, value: Any, priority: int) -> None: ...

class BaseSettings(MutableMapping[_SettingsKeyT, Any]):
    frozen: bool
    attributes: Incomplete
    def __init__(self, values: _SettingsInputT = None, priority: Union[int, str] = 'project') -> None: ...
    def __getitem__(self, opt_name: _SettingsKeyT) -> Any: ...
    def __contains__(self, name: Any) -> bool: ...
    def get(self, name: _SettingsKeyT, default: Any = None) -> Any: ...
    def getbool(self, name: _SettingsKeyT, default: bool = False) -> bool: ...
    def getint(self, name: _SettingsKeyT, default: int = 0) -> int: ...
    def getfloat(self, name: _SettingsKeyT, default: float = 0.0) -> float: ...
    def getlist(self, name: _SettingsKeyT, default: Optional[List[Any]] = None) -> List[Any]: ...
    def getdict(self, name: _SettingsKeyT, default: Optional[Dict[Any, Any]] = None) -> Dict[Any, Any]: ...
    def getdictorlist(self, name: _SettingsKeyT, default: Union[Dict[Any, Any], List[Any], Tuple[Any], None] = None) -> Union[Dict[Any, Any], List[Any]]: ...
    def getwithbase(self, name: _SettingsKeyT) -> BaseSettings: ...
    def getpriority(self, name: _SettingsKeyT) -> Optional[int]: ...
    def maxpriority(self) -> int: ...
    def __setitem__(self, name: _SettingsKeyT, value: Any) -> None: ...
    def set(self, name: _SettingsKeyT, value: Any, priority: Union[int, str] = 'project') -> None: ...
    def setdefault(self, name: _SettingsKeyT, default: Any = None, priority: Union[int, str] = 'project') -> Any: ...
    def setdict(self, values: _SettingsInputT, priority: Union[int, str] = 'project') -> None: ...
    def setmodule(self, module: Union[ModuleType, str], priority: Union[int, str] = 'project') -> None: ...
    def update(self, values: _SettingsInputT, priority: Union[int, str] = 'project') -> None: ...
    def delete(self, name: _SettingsKeyT, priority: Union[int, str] = 'project') -> None: ...
    def __delitem__(self, name: _SettingsKeyT) -> None: ...
    def copy(self) -> Self: ...
    def freeze(self) -> None: ...
    def frozencopy(self) -> Self: ...
    def __iter__(self) -> Iterator[_SettingsKeyT]: ...
    def __len__(self) -> int: ...
    def copy_to_dict(self) -> Dict[_SettingsKeyT, Any]: ...
    def pop(self, name: _SettingsKeyT, default: Any = ...) -> Any: ...

class Settings(BaseSettings):
    def __init__(self, values: _SettingsInputT = None, priority: Union[int, str] = 'project') -> None: ...

def iter_default_settings() -> Iterable[Tuple[str, Any]]: ...
def overridden_settings(settings: Mapping[_SettingsKeyT, Any]) -> Iterable[Tuple[str, Any]]: ...
