from scrapy import Spider as Spider
from scrapy.middleware import MiddlewareManager as MiddlewareManager
from scrapy.utils.conf import build_component_list as build_component_list
from scrapy.utils.defer import deferred_f_from_coro_f as deferred_f_from_coro_f
from twisted.internet.defer import Deferred as Deferred
from typing import Any

class ItemPipelineManager(MiddlewareManager):
    component_name: str
    def process_item(self, item: Any, spider: Spider) -> Deferred: ...
