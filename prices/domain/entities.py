from orchestrator.entities import Entity


class ProductPricing(Entity):
    def __init__(self, product_id, _id=None):
        self._id = _id
        self.product_id = product_id
        self._prices = {}

    def add_price(self, price):
        # if price in self._prices:
        #     raise PriceUniqueConstraint
        if price.price_type not in self._prices:
            self._prices[price.price_type] = {}
        self._prices[price.price_type][price.currency] = price

    def get_all_prices(self):
        prices = []
        for prices_by_currency in self._prices.values():
            prices += [p for p in prices_by_currency.values()]
        return prices

    def get_price(self, price_type, currency):
        try:
            price = self._prices[price_type][currency]
        except AttributeError:
            # raise PriceNotExists
            return None
        return price


# @TODO Это скорее всего value object
class Price(Entity):
    def __init__(self, price_type, currency, value: float, _id=None):
        self._id = _id
        self.price_type = price_type
        self.currency = currency
        self.value = value


class PriceType(Entity):
    def __init__(self, supplier_id, name, _id=None):
        self._id = _id
        self.supplier_id = supplier_id
        self.name = name


class Currency(Entity):
    def __init__(self, char_code, name, _id=None):
        self.char_code = char_code
        self.name = name
        self._id = _id

"""
product_id
price1


product -> get_price_attributes => price, currency, price_type, required_package_size


command_handler:
    Factory()
    
price_type.id = (supplier_id + name)


price:
    product_id, 
    
"""