from _typeshed import Incomplete
from scrapy import signals as signals
from scrapy.exceptions import NotConfigured as NotConfigured
from scrapy.mail import MailSender as MailSender

class StatsMailer:
    stats: Incomplete
    recipients: Incomplete
    mail: Incomplete
    def __init__(self, stats, recipients, mail) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    def spider_closed(self, spider): ...
