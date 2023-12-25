from _typeshed import Incomplete
from lxml.html import FormElement as FormElement, InputElement as InputElement, MultipleSelectOptions as MultipleSelectOptions, TextareaElement as TextareaElement
from scrapy.http.request import Request as Request
from scrapy.http.response.text import TextResponse as TextResponse
from scrapy.utils.python import is_listlike as is_listlike, to_bytes as to_bytes
from scrapy.utils.response import get_base_url as get_base_url
from typing import Iterable, List, Optional, Tuple, TypeVar, Union

FormRequestTypeVar = TypeVar('FormRequestTypeVar', bound='FormRequest')
FormdataKVType = Tuple[str, Union[str, Iterable[str]]]
FormdataType = Optional[Union[dict, List[FormdataKVType]]]

class FormRequest(Request):
    valid_form_methods: Incomplete
    def __init__(self, *args, formdata: FormdataType = None, **kwargs) -> None: ...
    @classmethod
    def from_response(cls, response: TextResponse, formname: Optional[str] = None, formid: Optional[str] = None, formnumber: int = 0, formdata: FormdataType = None, clickdata: Optional[dict] = None, dont_click: bool = False, formxpath: Optional[str] = None, formcss: Optional[str] = None, **kwargs) -> FormRequestTypeVar: ...
