from utils.queries import IQuery


class CartItems(IQuery):
    def __init__(self, cart_id: int):
        self.cart_id = cart_id

    def get(self, limit: int):
        pass
