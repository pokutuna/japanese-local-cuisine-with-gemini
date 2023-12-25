from _typeshed import Incomplete
from scrapy.utils.misc import arg_to_iter as arg_to_iter
from scrapy.utils.python import to_bytes as to_bytes

logger: Incomplete
COMMASPACE: str

class MailSender:
    smtphost: Incomplete
    smtpport: Incomplete
    smtpuser: Incomplete
    smtppass: Incomplete
    smtptls: Incomplete
    smtpssl: Incomplete
    mailfrom: Incomplete
    debug: Incomplete
    def __init__(self, smtphost: str = 'localhost', mailfrom: str = 'scrapy@localhost', smtpuser: Incomplete | None = None, smtppass: Incomplete | None = None, smtpport: int = 25, smtptls: bool = False, smtpssl: bool = False, debug: bool = False) -> None: ...
    @classmethod
    def from_settings(cls, settings): ...
    def send(self, to, subject, body, cc: Incomplete | None = None, attachs=(), mimetype: str = 'text/plain', charset: Incomplete | None = None, _callback: Incomplete | None = None): ...
