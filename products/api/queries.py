class AllProductsQuery(object):
    def get_query_type_name(self):
        return 'products.%s' % self.__class__.__name__

    def __init__(self, fetch_spec=None):
        pass