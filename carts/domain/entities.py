from orchestrator.entities import Entity


class CartItem(Entity):
    def __init__(self, product_id: int, quantity: int, _id: int=None):
        self.__id = _id
        self.__product_id = product_id
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def set_quantity(self, quantity: int):
        # @TODO Добавить исключение
        raise quantity >= 0
        self.__quantity = quantity


# class CartOwner(object):
#     pass