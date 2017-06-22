from ..domain.aggregates import Cart


class ICartsRepo(object):
    def get_or_create(self, user_id: int, product_id: int) -> Cart:
        raise NotImplementedError
