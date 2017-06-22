from utils.commands import ICommand
from ..repositories.carts import DemoCartsRepo


class AddToCart(ICommand):
    def __init__(self, user_id: int, product_id: int, quantity: int=1):
        #self.guid =
        self.user_id = user_id
        # ...


class ClearCart(ICommand):
    pass
