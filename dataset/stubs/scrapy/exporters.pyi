from _typeshed import Incomplete

__all__ = ['BaseItemExporter', 'PprintItemExporter', 'PickleItemExporter', 'CsvItemExporter', 'XmlItemExporter', 'JsonLinesItemExporter', 'JsonItemExporter', 'MarshalItemExporter']

class BaseItemExporter:
    def __init__(self, *, dont_fail: bool = False, **kwargs) -> None: ...
    def export_item(self, item) -> None: ...
    def serialize_field(self, field, name, value): ...
    def start_exporting(self) -> None: ...
    def finish_exporting(self) -> None: ...

class JsonLinesItemExporter(BaseItemExporter):
    file: Incomplete
    encoder: Incomplete
    def __init__(self, file, **kwargs) -> None: ...
    def export_item(self, item) -> None: ...

class JsonItemExporter(BaseItemExporter):
    file: Incomplete
    encoder: Incomplete
    first_item: bool
    def __init__(self, file, **kwargs) -> None: ...
    def start_exporting(self) -> None: ...
    def finish_exporting(self) -> None: ...
    def export_item(self, item) -> None: ...

class XmlItemExporter(BaseItemExporter):
    item_element: Incomplete
    root_element: Incomplete
    encoding: str
    xg: Incomplete
    def __init__(self, file, **kwargs) -> None: ...
    def start_exporting(self) -> None: ...
    def export_item(self, item) -> None: ...
    def finish_exporting(self) -> None: ...

class CsvItemExporter(BaseItemExporter):
    encoding: str
    include_headers_line: Incomplete
    stream: Incomplete
    csv_writer: Incomplete
    def __init__(self, file, include_headers_line: bool = True, join_multivalued: str = ',', errors: Incomplete | None = None, **kwargs) -> None: ...
    def serialize_field(self, field, name, value): ...
    def export_item(self, item) -> None: ...
    def finish_exporting(self) -> None: ...

class PickleItemExporter(BaseItemExporter):
    file: Incomplete
    protocol: Incomplete
    def __init__(self, file, protocol: int = 4, **kwargs) -> None: ...
    def export_item(self, item) -> None: ...

class MarshalItemExporter(BaseItemExporter):
    file: Incomplete
    def __init__(self, file, **kwargs) -> None: ...
    def export_item(self, item) -> None: ...

class PprintItemExporter(BaseItemExporter):
    file: Incomplete
    def __init__(self, file, **kwargs) -> None: ...
    def export_item(self, item) -> None: ...

class PythonItemExporter(BaseItemExporter):
    def serialize_field(self, field, name, value): ...
    def export_item(self, item): ...
