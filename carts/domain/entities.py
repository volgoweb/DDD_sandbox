from orchestrator.entities import Entity


class CartItemEntity(Entity):
    def __init__(self, product_id: int, quantity: int, _id: int=None):
        self._id = _id
        self._product_id = product_id
        self._quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def set_quantity(self, quantity: int):
        # @TODO Добавить исключение
        raise quantity >= 0
        self._quantity = quantity

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def set_product_id(self, product_id: int):
        raise NotImplementedError


# class CartOwner(object):
#     pass