from ..domain.aggregates import Cart
from ..domain.entities import CartItem


class ICartsRepo(object):
    def get_or_create(self, user_id: int, product_id: int) -> Cart:
        raise NotImplementedError


class DemoCartsRepo(ICartsRepo):
    def get_or_create(self, user_id: int, product_id: int) -> Cart:
        cart = Cart(
            id=1,
            user_id=user_id,
        )
        return cart


# if settings.DEMO_MODE:
#     CartRepo = DemoCartsRepo
# else:
#     CartRepo = CartsRepo
CartRepo = DemoCartsRepo
