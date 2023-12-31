from _typeshed import Incomplete
from typing import Any, Dict, Generator, Iterator, Optional

class Sitemap:
    type: Incomplete
    def __init__(self, xmltext: str) -> None: ...
    def __iter__(self) -> Iterator[Dict[str, Any]]: ...

def sitemap_urls_from_robots(robots_text: str, base_url: Optional[str] = None) -> Generator[str, Any, None]: ...
