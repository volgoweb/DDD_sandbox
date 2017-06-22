from django.utils.module_loading import import_string


class QueryHandlerRegister(object):
    # @TODO Перенести в settings
    _map = {
        'products.AllProductsQuery': 'products.query_handlers.base.AllProducts',
    }

    def get(self, query):
        # query_type = query.get_query_type_name()
        # path = self._map[query_type]
        # handler = import_string(path)
        # return handler
        from products.query_handlers.base import AllProducts
        return AllProducts

query_handler_register = QueryHandlerRegister()


def send_query(query):
    handler = query_handler_register.get(query)
    result = handler().execute(query)
    return result