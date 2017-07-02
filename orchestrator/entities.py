class Entity(object):
    """Базовый класс агрегата"""
    @property
    def id(self):
        return self._id

    @id.setter
    def set_id(self):
        raise NotImplemented
