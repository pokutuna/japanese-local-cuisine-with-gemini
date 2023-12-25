from OpenSSL import SSL
from _typeshed import Incomplete
from scrapy.utils.ssl import get_temp_key_info as get_temp_key_info, x509name_to_string as x509name_to_string
from twisted.internet._sslverify import ClientTLSOptions
from twisted.internet.ssl import AcceptableCiphers
from typing import Dict

logger: Incomplete
METHOD_TLS: str
METHOD_TLSv10: str
METHOD_TLSv11: str
METHOD_TLSv12: str
openssl_methods: Dict[str, int]

class ScrapyClientTLSOptions(ClientTLSOptions):
    verbose_logging: Incomplete
    def __init__(self, hostname: str, ctx: SSL.Context, verbose_logging: bool = False) -> None: ...

DEFAULT_CIPHERS: AcceptableCiphers
