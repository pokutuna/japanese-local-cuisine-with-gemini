from OpenSSL import SSL
from _typeshed import Incomplete
from scrapy.core.downloader.tls import DEFAULT_CIPHERS as DEFAULT_CIPHERS, ScrapyClientTLSOptions as ScrapyClientTLSOptions, openssl_methods as openssl_methods
from scrapy.settings import BaseSettings as BaseSettings
from scrapy.utils.misc import create_instance as create_instance, load_object as load_object
from twisted.internet._sslverify import ClientTLSOptions as ClientTLSOptions
from twisted.internet.ssl import CertificateOptions
from twisted.web.client import BrowserLikePolicyForHTTPS
from typing import Any, List, Optional

class ScrapyClientContextFactory(BrowserLikePolicyForHTTPS):
    tls_verbose_logging: Incomplete
    tls_ciphers: Incomplete
    def __init__(self, method: int = ..., tls_verbose_logging: bool = False, tls_ciphers: Optional[str] = None, *args: Any, **kwargs: Any) -> None: ...
    @classmethod
    def from_settings(cls, settings: BaseSettings, method: int = ..., *args: Any, **kwargs: Any): ...
    def getCertificateOptions(self) -> CertificateOptions: ...
    def getContext(self, hostname: Any = None, port: Any = None) -> SSL.Context: ...
    def creatorForNetloc(self, hostname: bytes, port: int) -> ClientTLSOptions: ...

class BrowserLikeContextFactory(ScrapyClientContextFactory):
    def creatorForNetloc(self, hostname: bytes, port: int) -> ClientTLSOptions: ...

class AcceptableProtocolsContextFactory:
    def __init__(self, context_factory: Any, acceptable_protocols: List[bytes]) -> None: ...
    def creatorForNetloc(self, hostname: bytes, port: int) -> ClientTLSOptions: ...

def load_context_factory_from_settings(settings, crawler): ...