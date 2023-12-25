from _typeshed import Incomplete
from typing import Any

class Link:
    url: Incomplete
    text: Incomplete
    fragment: Incomplete
    nofollow: Incomplete
    def __init__(self, url: str, text: str = '', fragment: str = '', nofollow: bool = False) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
