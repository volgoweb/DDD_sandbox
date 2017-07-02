from products.api.queries import AllProductsQuery
from orchestrator.query_handler_registers import send_query


def get_all_products():
    products = []
    q = AllProductsQuery()
    response = send_query(q)
    for dto in response:
        p = {
            'id': dto['id'],
            'name': dto['name'],
        }
        products.append(p)
    return products