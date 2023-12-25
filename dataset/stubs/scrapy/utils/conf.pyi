import os
from configparser import ConfigParser
from scrapy.exceptions import ScrapyDeprecationWarning as ScrapyDeprecationWarning, UsageError as UsageError
from scrapy.settings import BaseSettings as BaseSettings
from scrapy.utils.deprecate import update_classpath as update_classpath
from scrapy.utils.python import without_none_values as without_none_values
from typing import Any, Callable, Dict, List, MutableMapping, Optional, Union

def build_component_list(compdict: MutableMapping[Any, Any], custom: Any = None, convert: Callable[[Any], Any] = ...) -> List[Any]: ...
def arglist_to_dict(arglist: List[str]) -> Dict[str, str]: ...
def closest_scrapy_cfg(path: Union[str, os.PathLike] = '.', prevpath: Optional[Union[str, os.PathLike]] = None) -> str: ...
def init_env(project: str = 'default', set_syspath: bool = True) -> None: ...
def get_config(use_closest: bool = True) -> ConfigParser: ...
def get_sources(use_closest: bool = True) -> List[str]: ...
def feed_complete_default_values_from_settings(feed: Dict[str, Any], settings: BaseSettings) -> Dict[str, Any]: ...
def feed_process_params_from_cli(settings: BaseSettings, output: List[str], output_format: Optional[str] = None, overwrite_output: Optional[List[str]] = None) -> Dict[str, Dict[str, Any]]: ...