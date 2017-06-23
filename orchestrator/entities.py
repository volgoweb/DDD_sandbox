class Entity(object):
    """Базовый класс агрегата"""
    @property
    def id(self):
        return self._id

    @property.setter(id)
    def set_id(self):
        raise NotImplemented
