from _typeshed import Incomplete
from scrapy.commands import ScrapyCommand as ScrapyCommand
from scrapy.exceptions import UsageError as UsageError
from scrapy.utils.template import render_templatefile as render_templatefile, string_camelcase as string_camelcase

TEMPLATES_TO_RENDER: Incomplete
IGNORE: Incomplete

class Command(ScrapyCommand):
    requires_project: bool
    default_settings: Incomplete
    def syntax(self): ...
    def short_desc(self): ...
    exitcode: int
    def run(self, args, opts) -> None: ...
    @property
    def templates_dir(self) -> str: ...
