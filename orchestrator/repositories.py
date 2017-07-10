class IRepository(object):
    def get_by_id(self, _id):
        raise NotImplementedError

    def save_one(self, entity):
        raise NotImplementedError
