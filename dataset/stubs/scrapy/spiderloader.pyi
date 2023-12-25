from _typeshed import Incomplete
from scrapy import Request as Request, Spider as Spider
from scrapy.interfaces import ISpiderLoader as ISpiderLoader
from scrapy.settings import BaseSettings as BaseSettings
from scrapy.utils.misc import walk_modules as walk_modules
from scrapy.utils.spider import iter_spider_classes as iter_spider_classes
from typing import List, Type
from typing_extensions import Self

class SpiderLoader:
    spider_modules: Incomplete
    warn_only: Incomplete
    def __init__(self, settings: BaseSettings) -> None: ...
    @classmethod
    def from_settings(cls, settings: BaseSettings) -> Self: ...
    def load(self, spider_name: str) -> Type[Spider]: ...
    def find_by_request(self, request: Request) -> List[str]: ...
    def list(self) -> List[str]: ...
