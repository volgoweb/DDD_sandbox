from ..domain.repository_interfaces import IProductRepository


class ProductsRepository(IProductRepository):
    def all(self, fetch_spec=None):
        return [
            {
                'id': 1,
                'name': 'Product # 1',
            },
            {
                'id': 2,
                'name': 'Product # 2',
            },
            {
                'id': 3,
                'name': 'Product # 3',
            },
        ]