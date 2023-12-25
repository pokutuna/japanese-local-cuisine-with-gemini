import argparse
from _typeshed import Incomplete
from scrapy.commands import BaseRunSpiderCommand as BaseRunSpiderCommand, ScrapyCommand as ScrapyCommand, ScrapyHelpFormatter as ScrapyHelpFormatter
from scrapy.crawler import CrawlerProcess as CrawlerProcess
from scrapy.exceptions import UsageError as UsageError
from scrapy.utils.misc import walk_modules as walk_modules
from scrapy.utils.project import get_project_settings as get_project_settings, inside_project as inside_project
from scrapy.utils.python import garbage_collect as garbage_collect

class ScrapyArgumentParser(argparse.ArgumentParser): ...

def execute(argv: Incomplete | None = None, settings: Incomplete | None = None) -> None: ...
