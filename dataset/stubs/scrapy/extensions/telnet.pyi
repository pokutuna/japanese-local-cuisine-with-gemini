from _typeshed import Incomplete
from scrapy import signals as signals
from scrapy.exceptions import NotConfigured as NotConfigured
from scrapy.utils.decorators import defers as defers
from scrapy.utils.engine import print_engine_status as print_engine_status
from scrapy.utils.reactor import listen_tcp as listen_tcp
from scrapy.utils.trackref import print_live_refs as print_live_refs
from twisted.internet import protocol

TWISTED_CONCH_AVAILABLE: bool
logger: Incomplete
update_telnet_vars: Incomplete

class TelnetConsole(protocol.ServerFactory):
    crawler: Incomplete
    noisy: bool
    portrange: Incomplete
    host: Incomplete
    username: Incomplete
    password: Incomplete
    def __init__(self, crawler) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    port: Incomplete
    def start_listening(self) -> None: ...
    def stop_listening(self) -> None: ...
    def protocol(self): ...
