import itemloaders
from _typeshed import Incomplete
from scrapy.item import Item as Item
from scrapy.selector import Selector as Selector

class ItemLoader(itemloaders.ItemLoader):
    default_item_class = Item
    default_selector_class = Selector
    def __init__(self, item: Incomplete | None = None, selector: Incomplete | None = None, response: Incomplete | None = None, parent: Incomplete | None = None, **context) -> None: ...
