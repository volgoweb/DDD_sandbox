from ..adapters import prices as prices_adapter

class Cart(object):
    def __init__(self, owner: CartOwner):
        """
        :param owner: Так как в некоторых проектах у каждого юзера должны быть разные корзины 
        для каждого менеджера контрагента,
        а в остальных - общая корзина на всех менеджеров контрагента, то owner в этом контексте - владелец, который 
        может быть как сущностью contractor, так и сущностью менеджер контраагента
        """
        self._items = []
        self.sum_of_items = None
        self.sum_total = None

    def get_items(self) -> list:
        pass

    def add_item(self, item: CartItem):
        pass

    def calculate_sum_of_items(self):
        pass

    def apply_coupons(self):
        prices_adapter.apply_coupons_for_cart_sum_total(self)