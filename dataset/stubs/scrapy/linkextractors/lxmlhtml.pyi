from _typeshed import Incomplete
from scrapy.link import Link as Link
from scrapy.linkextractors import IGNORED_EXTENSIONS as IGNORED_EXTENSIONS, re as re
from scrapy.utils.misc import arg_to_iter as arg_to_iter, rel_has_nofollow as rel_has_nofollow
from scrapy.utils.response import get_base_url as get_base_url
from scrapy.utils.url import url_has_any_extension as url_has_any_extension, url_is_from_any_domain as url_is_from_any_domain

logger: Incomplete
XHTML_NAMESPACE: str

class LxmlParserLinkExtractor:
    scan_tag: Incomplete
    scan_attr: Incomplete
    process_attr: Incomplete
    unique: Incomplete
    strip: Incomplete
    link_key: Incomplete
    def __init__(self, tag: str = 'a', attr: str = 'href', process: Incomplete | None = None, unique: bool = False, strip: bool = True, canonicalized: bool = False) -> None: ...
    def extract_links(self, response): ...

class LxmlLinkExtractor:
    link_extractor: Incomplete
    allow_res: Incomplete
    deny_res: Incomplete
    allow_domains: Incomplete
    deny_domains: Incomplete
    restrict_xpaths: Incomplete
    canonicalize: Incomplete
    deny_extensions: Incomplete
    restrict_text: Incomplete
    def __init__(self, allow=(), deny=(), allow_domains=(), deny_domains=(), restrict_xpaths=(), tags=('a', 'area'), attrs=('href',), canonicalize: bool = False, unique: bool = True, process_value: Incomplete | None = None, deny_extensions: Incomplete | None = None, restrict_css=(), strip: bool = True, restrict_text: Incomplete | None = None) -> None: ...
    def matches(self, url): ...
    def extract_links(self, response): ...
