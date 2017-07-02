from orchestrator.aggregates import Aggregate
from .value_objects import Price


class Product(Aggregate):
    def __init__(self, name: str, _id: int=None):
        self._id = _id
        self.name = name


class ProductModification(object):
    """Это сущность не является целиком модификацией как в старой агоре.
    Она содержит лишь ту часть данных и логики, которая нужна в контексте продажи."""
    def __init__(self, id_: int, product: Product, name: str):
        self.id = id_
        self.product = product
        self.name = name
        self._prices = []

    def add_price(self, price: Price):
        self._prices.append(price)
