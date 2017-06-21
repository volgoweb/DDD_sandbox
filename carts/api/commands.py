from utils.commands import ICommand
from ..repositories.carts import CartRepo


class AddToCart(ICommand):
    def execute(self, user_id: int, product_id: int, quantity: int=1):
        # user = UserRepo.get_by_id(user_id)
        # product_modification = ProductModificationRepo.get_by_id(product_modification_id)
        cart = CartRepo.get_or_create(user_id)
        create_item_command = CreateItem()
        item = create_item_command.execute(product_id=product_id, quantity=quantity)
        cart.add_item(item)
        pass


class ClearCart(ICommand):
    pass


class CreateItem(ICommand):
    def execute(self, user_id: int, product_id: int, quantity: int=1):
        pass
        # Getting price for this user
        # CartItemRepo.create(...)
