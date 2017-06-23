from orchestrator.entities import Entity


class CartItem(Entity):
    def __init__(self, product_id: int, _id: int=None):
        self._id = _id
        self._product_id = product_id

    @property.getter('quan')
    def set_quantity(self, quantity: int):
        # @TODO Добавить исключение
        raise quantity >= 0
        self._quantity = quantity


# class CartOwner(object):
#     pass