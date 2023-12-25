import json
from scrapy.http import Request as Request, Response as Response
from typing import Any

class ScrapyJSONEncoder(json.JSONEncoder):
    DATE_FORMAT: str
    TIME_FORMAT: str
    def default(self, o: Any) -> Any: ...

class ScrapyJSONDecoder(json.JSONDecoder): ...
