from ..domain.repository_interfaces import IPriceTypeRepo, ICurrencyRepo, IProductPricingRepo
from ..domain.entities import ProductPricing, Price, PriceType, Currency


class DummyPriceTypeRepo(IPriceTypeRepo):
    data = {
        1: {
            'id': 1,
            'supplier_id': 1,
            'name': 'Retail 1 sup1',
        },
        2: {
            'id': 2,
            'supplier_id': 1,
            'name': 'Wholesale 1 sup1',
        },
        3: {
            'id': 3,
            'supplier_id': 2,
            'name': 'Retail 1 sup2',
        },
        4: {
            'id': 4,
            'supplier_id': 2,
            'name': 'Wholesale 1 sup2',
        },
    }

    def get_by_id(self, _id):
        try:
            dto = self.data[_id]

            return dto
        except AttributeError:
            # raise PriceTypeNotFound
            return None

    def save_one(self, entity):
        self.data[entity.id] = {
            'id': entity.id,
            'supplier_id': entity.supplier_id,
            'name': entity.name,
        }


class DummyCurrencyRepo(ICurrencyRepo):
    data = {
        1: {
            'id': 1,
            'supplier_id': 1,
            'name': 'Retail 1 sup1',
        },
        2: {
            'id': 2,
            'supplier_id': 1,
            'name': 'Wholesale 1 sup1',
        },
        3: {
            'id': 3,
            'supplier_id': 2,
            'name': 'Retail 1 sup2',
        },
        4: {
            'id': 4,
            'supplier_id': 2,
            'name': 'Wholesale 1 sup2',
        },
    }

    def get_by_id(self, _id):
        try:
            dto = self.data[_id]

            return dto
        except AttributeError:
            # raise PriceTypeNotFound
            return None

    def save_one(self, entity):
        self.data[entity.id] = {
            'id': entity.id,
            'supplier_id': entity.supplier_id,
            'name': entity.name,
        }


# class DummyPriceRepo(IPriceTypeRepo):
#     data = {
#         1: {
#             'id': 1,
#             'price_type_id': 1,
#             'currency_id': 1,
#             'value': 124.33,
#         },
#         2: {
#             'id': 2,
#             'price_type_id': 2,
#             'currency_id': 1,
#             'value': 120.50,
#         },
#         3: {
#             'id': 3,
#             'price_type_id': 3,
#             'currency_id': 1,
#             'value': 100.80,
#         },
#     }
#
#     def get_by_id(self, _id):
#         try:
#             dto = self.data[_id]
#             return dto
#         except AttributeError:
#             # raise PriceTypeNotFound
#             return None
#
#     def save_one(self, entity):
#         self.data[entity.id] = {
#             'id': entity.id,
#             'price_type_id': entity.price_type_id,
#             'currency_id': entity.currency_id,
#             'value': entity.value,
#         }


class DummyProductPricingRepo(IProductPricingRepo):
    data = {
        1: {
            'id': 1,
            'product_id': 1,
            'price_type_id': 1,
            'currency_id': 1,
            'value': 124.33,
        },
        2: {
            'id': 2,
            'product_id': 1,
            'price_type_id': 2,
            'currency_id': 1,
            'value': 120.50,
        },
        3: {
            'id': 3,
            'product_id': 2,
            'price_type_id': 3,
            'currency_id': 1,
            'value': 100.80,
        },
    }

    def get_by_id(self, _id):
        try:
            raw = self.data[_id]
        except AttributeError:
            # raise PriceTypeNotFound
            return None
        entity = ProductPricing(
            product_id=raw['product_id'],
            _id=raw['id'],
        )
        return entity

    def get_by_product_id(self, product_id: int, return_raw=False):
        raws = [d for d in self.data.values() if d['product_id'] == product_id]
        if return_raw:
            return raws
        product_pricing = ProductPricing(product_id)
        for r in raws:
            price_type = PriceType(r['price_type_id'])
            currency = Currency(r['currency_id'])
            price = Price(
                price_type=price_type,
                currency=currency,
                value=r['value']
            )
            product_pricing.add_price(price)
        return product_pricing

    def get_by_product_ids(self, product_ids: tuple, return_raw=False):
        product_pricing_list = []
        for pid in product_ids:
            pp = self.get_by_product_id(pid, return_raw)
            product_pricing_list.append(pp)
        return product_pricing_list

    def all(self, return_raw=False):
        by_product_id = self._get_data_by_product_id()
        if return_raw:
            return by_product_id

    def _get_data_by_product_id(self):
        by_product_id = {}
        for i, row in self.data.items():
            product_id = row['product_id']
            if product_id not in by_product_id:
                by_product_id[product_id] = []
            by_product_id[product_id].append(row)
        return by_product_id

    def save_one(self, entity):
        self.remove_all_with_product_id(entity.product_id)
        for price in entity.get_all_prices():
            raw = {
                'product_id': entity.product_id,
                'price_type_id': price.price_type.id,
                'currency_id': price.currency.id,
                'value': price.value,
            }
            max_index = max(self.data.keys())
            self.data[max_index] = raw

    def remove_all_with_product_id(self, product_id):
        for k, data in self.data.items():
            if data['product_id'] == product_id:
                del self.data[k]
