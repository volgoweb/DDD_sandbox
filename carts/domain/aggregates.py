from orchestrator.aggregates import Aggregate
from ..adapters import prices as prices_adapter
from .entities import CartItem


# @TODO Вероятно стоит наследоваться от BaseEntity or Entity
class Cart(Aggregate):
    def __init__(self, user_id, _id: int=None):
        """
        :param owner: Так как в некоторых проектах у каждого юзера должны быть разные корзины 
        для каждого менеджера контрагента,
        а в остальных - общая корзина на всех менеджеров контрагента, то owner в этом контексте - владелец, который 
        может быть как сущностью contractor, так и сущностью менеджер контраагента
        """
        self.__id = _id
        self.__items = []
        self.__sum_of_items = None
        self.__sum_total = None

    @property
    def items(self):
        return self.__items

    @items.setter
    def set_items(self):
        raise

    def get_items(self) -> list:
        pass

    def add_item(self, item: CartItem):
        pass

    def calculate_sum_of_items(self):
        pass

    def apply_coupons(self):
        prices_adapter.apply_coupons_for_cart_sum_total(self)
