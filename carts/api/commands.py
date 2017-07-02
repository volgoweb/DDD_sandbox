from utils.commands import ICommand


class AddToCart(ICommand):
    @classmethod
    def get_command_type_name(cls):
        return 'carts.AddToCart'

    def __init__(self, user_id: int, product_id: int, quantity: int=1):
        #self.guid =
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity


class ClearCart(ICommand):
    pass
