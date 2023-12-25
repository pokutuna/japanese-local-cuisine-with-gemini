from _typeshed import Incomplete
from scrapy.contracts import Contract as Contract
from scrapy.exceptions import ContractFail as ContractFail
from scrapy.http import Request as Request

class UrlContract(Contract):
    name: str
    def adjust_request_args(self, args): ...

class CallbackKeywordArgumentsContract(Contract):
    name: str
    def adjust_request_args(self, args): ...

class ReturnsContract(Contract):
    name: str
    object_type_verifiers: Incomplete
    obj_name: Incomplete
    obj_type_verifier: Incomplete
    min_bound: Incomplete
    max_bound: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def post_process(self, output) -> None: ...

class ScrapesContract(Contract):
    name: str
    def post_process(self, output) -> None: ...
