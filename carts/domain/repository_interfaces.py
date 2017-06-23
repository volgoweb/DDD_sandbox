# @TODO решить как писать интерфейс репо при переопределении репозиториев и сущностей.

class ICartsRepo(object):
    def get_by_user_id(self, user_id: int):
        raise NotImplementedError

    def add_one(self, cart):
        raise NotImplementedError

    def update(self, cart):
        pass

    def delete(self, cart):
        pass
