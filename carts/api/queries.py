from utils.queries import IQuery


class CartOfUserQuery(IQuery):
    @classmethod
    def get_query_type_name(cls):
        return 'carts.CartOfUser'

    def __init__(self, user_id: int):
        self.user_id = user_id
