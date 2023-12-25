from _typeshed import Incomplete
from scrapy import signals as signals
from scrapy.exceptions import NotConfigured as NotConfigured
from scrapy.mail import MailSender as MailSender
from scrapy.utils.engine import get_engine_status as get_engine_status

logger: Incomplete

class MemoryUsage:
    resource: Incomplete
    crawler: Incomplete
    warned: bool
    notify_mails: Incomplete
    limit: Incomplete
    warning: Incomplete
    check_interval: Incomplete
    mail: Incomplete
    def __init__(self, crawler) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    def get_virtual_size(self): ...
    tasks: Incomplete
    def engine_started(self) -> None: ...
    def engine_stopped(self) -> None: ...
    def update(self) -> None: ...
