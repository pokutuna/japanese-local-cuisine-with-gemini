from _typeshed import Incomplete
from scrapy.commands import ScrapyCommand as ScrapyCommand

class Command(ScrapyCommand):
    requires_project: bool
    default_settings: Incomplete
    def short_desc(self): ...
    def run(self, args, opts) -> None: ...
