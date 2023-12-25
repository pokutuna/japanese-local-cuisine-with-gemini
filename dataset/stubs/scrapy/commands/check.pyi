from _typeshed import Incomplete
from scrapy.commands import ScrapyCommand as ScrapyCommand
from scrapy.contracts import ContractsManager as ContractsManager
from scrapy.utils.conf import build_component_list as build_component_list
from scrapy.utils.misc import load_object as load_object, set_environ as set_environ
from unittest import TextTestResult as _TextTestResult

class TextTestResult(_TextTestResult):
    def printSummary(self, start, stop) -> None: ...

class Command(ScrapyCommand):
    requires_project: bool
    default_settings: Incomplete
    def syntax(self): ...
    def short_desc(self): ...
    def add_options(self, parser) -> None: ...
    exitcode: Incomplete
    def run(self, args, opts): ...
