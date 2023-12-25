from scrapy.exceptions import ScrapyDeprecationWarning as ScrapyDeprecationWarning
from typing import Any, Dict, List, Optional, Tuple, Type, overload

def attribute(obj: Any, oldattr: str, newattr: str, version: str = '0.12') -> None: ...
def create_deprecated_class(name: str, new_class: type, clsdict: Optional[Dict[str, Any]] = None, warn_category: Type[Warning] = ..., warn_once: bool = True, old_class_path: Optional[str] = None, new_class_path: Optional[str] = None, subclass_warn_message: str = '{cls} inherits from deprecated class {old}, please inherit from {new}.', instance_warn_message: str = '{cls} is deprecated, instantiate {new} instead.') -> type: ...

DEPRECATION_RULES: List[Tuple[str, str]]

@overload
def update_classpath(path: str) -> str: ...
@overload
def update_classpath(path: Any) -> Any: ...
def method_is_overridden(subclass: type, base_class: type, method_name: str) -> bool: ...