from _typeshed import Incomplete
from collections.abc import Generator
from scrapy import signals as signals
from scrapy.exceptions import NotConfigured as NotConfigured
from scrapy.http import Request as Request, Response as Response
from scrapy.utils.misc import load_object as load_object
from scrapy.utils.python import to_unicode as to_unicode
from scrapy.utils.url import strip_url as strip_url
from typing import Tuple

LOCAL_SCHEMES: Incomplete
POLICY_NO_REFERRER: str
POLICY_NO_REFERRER_WHEN_DOWNGRADE: str
POLICY_SAME_ORIGIN: str
POLICY_ORIGIN: str
POLICY_STRICT_ORIGIN: str
POLICY_ORIGIN_WHEN_CROSS_ORIGIN: str
POLICY_STRICT_ORIGIN_WHEN_CROSS_ORIGIN: str
POLICY_UNSAFE_URL: str
POLICY_SCRAPY_DEFAULT: str

class ReferrerPolicy:
    NOREFERRER_SCHEMES: Tuple[str, ...]
    name: str
    def referrer(self, response_url, request_url) -> None: ...
    def stripped_referrer(self, url): ...
    def origin_referrer(self, url): ...
    def strip_url(self, url, origin_only: bool = False): ...
    def origin(self, url): ...
    def potentially_trustworthy(self, url): ...
    def tls_protected(self, url): ...

class NoReferrerPolicy(ReferrerPolicy):
    name: str
    def referrer(self, response_url, request_url) -> None: ...

class NoReferrerWhenDowngradePolicy(ReferrerPolicy):
    name: str
    def referrer(self, response_url, request_url): ...

class SameOriginPolicy(ReferrerPolicy):
    name: str
    def referrer(self, response_url, request_url): ...

class OriginPolicy(ReferrerPolicy):
    name: str
    def referrer(self, response_url, request_url): ...

class StrictOriginPolicy(ReferrerPolicy):
    name: str
    def referrer(self, response_url, request_url): ...

class OriginWhenCrossOriginPolicy(ReferrerPolicy):
    name: str
    def referrer(self, response_url, request_url): ...

class StrictOriginWhenCrossOriginPolicy(ReferrerPolicy):
    name: str
    def referrer(self, response_url, request_url): ...

class UnsafeUrlPolicy(ReferrerPolicy):
    name: str
    def referrer(self, response_url, request_url): ...

class DefaultReferrerPolicy(NoReferrerWhenDowngradePolicy):
    NOREFERRER_SCHEMES: Tuple[str, ...]
    name: str

class RefererMiddleware:
    default_policy: Incomplete
    def __init__(self, settings: Incomplete | None = None) -> None: ...
    @classmethod
    def from_crawler(cls, crawler): ...
    def policy(self, resp_or_url, request): ...
    def process_spider_output(self, response, result, spider): ...
    async def process_spider_output_async(self, response, result, spider) -> Generator[Incomplete, None, None]: ...
    def request_scheduled(self, request, spider) -> None: ...
