from orchestrator.repositories import IRepository


class IPriceTypeRepo(IRepository):
    pass


class ICurrencyRepo(IRepository):
    pass


class IProductPricingRepo(IRepository):
    def get_by_product_id(self, product_id: int):
        raise NotImplementedError

    def get_by_product_ids(self, product_ids: list):
        raise NotImplementedError

