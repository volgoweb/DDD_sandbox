from orchestrator.aggregates import Aggregate
from ..adapters import prices as prices_adapter
from .entities import CartItemEntity
from ..exceptions import ProductInCartUniqueConstraint


# @TODO Вероятно стоит наследоваться от BaseEntity or Entity
class CartAggregate(Aggregate):
    def __init__(self, user_id, _id: int=None):
        """
        :param owner: Так как в некоторых проектах у каждого юзера должны быть разные корзины 
        для каждого менеджера контрагента,
        а в остальных - общая корзина на всех менеджеров контрагента, то owner в этом контексте - владелец, который 
        может быть как сущностью contractor, так и сущностью менеджер контраагента
        """
        self._id = _id
        self._user_id = user_id
        self._items = []
        self._sum_of_items = None

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def set_user_id(self):
        raise NotImplementedError

    @property
    def items(self):
        return self._items

    @items.setter
    def set_items(self):
        raise

    def add_item(self, item: CartItemEntity):
        if self.does_exist_item(item):
            raise ProductInCartUniqueConstraint
        self._items.append(item)

    def does_exist_item(self, item):
        if item in self.items:
            return True
        product_ids = [im.product_id for im in self.items]
        if item.product_id in product_ids:
            return True
        return False

    def calculate_sum_of_items(self):
        pass

    def apply_coupons(self):
        prices_adapter.apply_coupons_for_cart_sum_total(self)
