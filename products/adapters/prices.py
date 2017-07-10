from prices.api.queries import GetProductPricingForManyProducts, GetProductPricingForAllProducts
from orchestrator.query_handler_registers import send_query


def get_product_prices_adapter(product_ids: tuple):
    query = GetProductPricingForManyProducts(product_ids)
    response = send_query(query)
    return response


def get_all_product_prices_adapter():
    query = GetProductPricingForAllProducts()
    response = send_query(query)
    return response
