from ..repositories.register import repository_register
from orchestrator.query_handler_registers import IQueryHandler


class BaseHandler(IQueryHandler):
    def __init__(self):
        repo_cls = repository_register.get('ProductsRepository')
        self.products_repo = repo_cls()


class AllProducts(BaseHandler):
    def __init__(self):
        repo_cls = repository_register.get('ProductsRepository')
        self.products_repo = repo_cls()

    def handle(self, query):
        return self.products_repo.all()


class ProductsByIds(BaseHandler):
    def handle(self, query):
        raws = self.products_repo.filter_by_ids(query.ids)
        product_DTOs = []
        for r in raws:
            # @TODO пока тупо копируем, потому что репо отдает dummy
            dto = r
            product_DTOs.append(dto)
        return product_DTOs
