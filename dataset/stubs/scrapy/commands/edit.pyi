from _typeshed import Incomplete
from scrapy.commands import ScrapyCommand as ScrapyCommand
from scrapy.exceptions import UsageError as UsageError

class Command(ScrapyCommand):
    requires_project: bool
    default_settings: Incomplete
    def syntax(self): ...
    def short_desc(self): ...
    def long_desc(self): ...
    exitcode: Incomplete
    def run(self, args, opts): ...