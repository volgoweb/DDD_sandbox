from utils.commands import ICommand
from ...repositories import ProductModificationRepo, UserRepo, CartRepo


class AddToCart(ICommand):
    def execute(self, user_id: int, product_modification_id: int, quantity: int=1):
        user = UserRepo.get_by_id(user_id)
        product_modification = ProductModificationRepo.get_by_id(product_modification_id)
        cart = CartRepo.get_by_user_id(user_id)


class ClearCart(ICommand):
    pass
