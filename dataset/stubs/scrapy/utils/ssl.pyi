from OpenSSL.crypto import X509Name as X509Name
from scrapy.utils.python import to_unicode as to_unicode
from typing import Any, Optional

def ffi_buf_to_string(buf: Any) -> str: ...
def x509name_to_string(x509name: X509Name) -> str: ...
def get_temp_key_info(ssl_object: Any) -> Optional[str]: ...
def get_openssl_version() -> str: ...