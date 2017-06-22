from ..domain.aggregates import Cart
from ..domain.entities import CartItem
from ..domain.repository_interfaces import ICartsRepo


class DemoCartsRepo(ICartsRepo):
    def get_or_create(self, user_id: int, product_id: int) -> Cart:
        cart = Cart(
            id=1,
            user_id=user_id,
        )
        return cart
