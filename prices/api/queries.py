from utils.queries import IQuery


class GetProductPricingForOneProduct(IQuery):
    def __init__(self, product_id: int):
        self.product_id = product_id

    @classmethod
    def get_query_type_name(cls):
        return 'prices.GetProductPricingForOneProduct'


class GetProductPricingForManyProducts(IQuery):
    def __init__(self, product_id: int):
        self.product_id = product_id

    @classmethod
    def get_query_type_name(cls):
        return 'prices.GetProductPricingForManyProducts'


class GetProductPricingForAllProducts(IQuery):
    @classmethod
    def get_query_type_name(cls):
        return 'prices.GetProductPricingForAllProducts'
