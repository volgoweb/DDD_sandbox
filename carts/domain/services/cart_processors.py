from ...adapters.products import GetProductsByIdsAdapter


class ICartItemProcessor(object):
    def run(self, cart):
        raise NotImplementedError


class AddProductNameIntoCartItems(ICartItemProcessor):
    # @TODO Пока не понял, нужно ли это делать с сущностями... может добавлять такие данные уже в DTO
    def run(self, cart):
        products_ids = [i.product_id for i in cart.items]
        products = self.get_products_by_ids(products_ids)
        products_by_id = {p['id']: p for p in products}
        for item in cart.items:
            product = products_by_id[item.product_id]
            item.product_name = product['name']
        return cart

    @staticmethod
    def get_products_by_ids(ids):
        adapter = GetProductsByIdsAdapter()
        result = adapter.request(ids)
        return result
