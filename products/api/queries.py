from utils.queries.interfaces import IQuery


class AllProductsQuery(IQuery):
    @classmethod
    def get_query_type_name(cls):
        return 'products.AllProductsQuery'

    def __init__(self, fetch_spec=None):
        pass


class ProductNameFetchSpec(object):
    fields = [
        'id',
        'name',
    ]


class ProductsByIdsQuery(IQuery):
    @classmethod
    def get_query_type_name(cls):
        return 'products.ProductsByIds'

    def __init__(self, ids: list, fetch_spec=None):
        self.ids = ids
        self.fetch_spec = fetch_spec
