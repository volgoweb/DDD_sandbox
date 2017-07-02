from ..domain.repository_interfaces import IProductRepository


class ProductsRepository(IProductRepository):
    _products = {
        1: {
            'id': 1,
            'name': 'Product # 1',
        },
        2: {
            'id': 2,
            'name': 'Product # 2',
        },
        3: {
            'id': 3,
            'name': 'Product # 3',
        },
    }

    def all(self, fetch_spec=None):
        return self._products.values()

    def filter_by_ids(self, ids: list):
        l = [p for pk, p in self._products.items() if pk in ids]
        return l
