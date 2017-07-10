from orchestrator.query_handler_registers import IQueryHandler
from ..repositories.register import repository_register


class GetProductPricingForOneProductHandler(IQueryHandler):
    def __init__(self):
        repo_cls = repository_register.get('ProductPricing')
        self.repo = repo_cls()

    def handle(self, query):
        raws = self.repo.get_by_product_id(query.product_id, return_raw=True)
        return raws


class GetProductPricingForManyProductsHandler(IQueryHandler):
    def __init__(self):
        repo_cls = repository_register.get('ProductPricing')
        self.repo = repo_cls()

    def handle(self, query):
        return self.repo.get_by_product_ids(query.product_ids, return_raw=True)


class GetProductPricingForAllProductsHandler(IQueryHandler):
    def __init__(self):
        repo_cls = repository_register.get('ProductPricing')
        self.repo = repo_cls()

    def handle(self, query):
        return self.repo.all(return_raw=True)
