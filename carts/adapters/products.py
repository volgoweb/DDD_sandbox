from products.api.queries import ProductsByIdsQuery
from orchestrator.query_handler_registers import send_query


class GetProductsByIdsAdapter(object):
    def request(self, ids: list):
        q = ProductsByIdsQuery(ids)
        response = send_query(q)
        return response
