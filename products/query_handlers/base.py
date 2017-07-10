from ..repositories.register import repository_register
from ..adapters.prices import get_product_prices_adapter, get_all_product_prices_adapter
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
        raws = self.products_repo.all()
        prices_by_product_id = self._get_prices_of_all_products()
        product_DTOs = []
        for r in raws:
            # @TODO пока тупо копируем, потому что репо отдает dummy
            dto = r
            product_id = r['id']
            dto['prices'] = prices_by_product_id.get(product_id, [])
            # Пока без логики определения цены, которую нужно показать
            dto['main_price'] = dto['prices'].pop() if dto['prices'] else {}
            product_DTOs.append(dto)
        return product_DTOs

    @staticmethod
    def _get_prices_of_all_products():
        prices = get_all_product_prices_adapter()
        prices_by_product_id = {}
        for product_id, prod_prices in prices.items():

            prices_by_product_id[product_id] = prod_prices
        return prices_by_product_id


class ProductsByIds(BaseHandler):
    def handle(self, query):
        raws = self.products_repo.filter_by_ids(query.ids)
        prices_by_product_id = self._get_prices_of_products(query.ids)
        product_DTOs = []
        for r in raws:
            # @TODO пока тупо копируем, потому что репо отдает dummy
            dto = r
            product_id = r['id']
            r['prices'] = prices_by_product_id[product_id]
            product_DTOs.append(dto)
        return product_DTOs

    def _get_prices_of_products(self, product_ids: tuple):
        prices = get_product_prices_adapter(product_ids)
        prices_by_product_id = {}
        for prod_prices in prices:
            if prod_prices and prod_prices[0]['product_id']:
                product_id = prod_prices[0]['product_id']
                prices_by_product_id[product_id] = prod_prices
        return prices_by_product_id

