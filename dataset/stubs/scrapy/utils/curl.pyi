import argparse
from _typeshed import Incomplete

class DataAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string: Incomplete | None = None) -> None: ...

class CurlParser(argparse.ArgumentParser):
    def error(self, message) -> None: ...

curl_parser: Incomplete
safe_to_ignore_arguments: Incomplete

def curl_to_request_kwargs(curl_command: str, ignore_unknown_options: bool = True) -> dict: ...
