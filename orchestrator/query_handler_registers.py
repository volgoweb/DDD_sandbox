from django.utils.module_loading import import_string


class IQueryHandler(object):
    def handle(self, query):
        raise NotImplementedError


class QueryHandlerRegister(object):
    # @TODO Перенести в settings
    _map = {
        'products.AllProductsQuery': 'products.query_handlers.base.AllProducts',
        'carts.CartOfUser': 'carts.query_handlers.base.CartOfUser',
        'products.ProductsByIds': 'products.query_handlers.base.ProductsByIds',
        'prices.GetProductPricingForManyProducts': 'prices.query_handlers.base.GetProductPricingForManyProducts',
        'prices.GetProductPricingForAllProducts': 'prices.query_handlers.base.GetProductPricingForAllProductsHandler',
    }

    def get(self, query):
        query_type = query.get_query_type_name()
        path = self._map[query_type]
        handler = import_string(path)
        return handler


query_handler_register = QueryHandlerRegister()


def send_query(query):
    handler = query_handler_register.get(query)
    result = handler().handle(query)
    return result

