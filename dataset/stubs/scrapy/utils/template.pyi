from _typeshed import Incomplete
from os import PathLike
from typing import Any, Union

def render_templatefile(path: Union[str, PathLike], **kwargs: Any) -> None: ...

CAMELCASE_INVALID_CHARS: Incomplete

def string_camelcase(string: str) -> str: ...
