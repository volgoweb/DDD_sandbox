class Entity(object):
    """Базовый класс агрегата"""
    @property
    def id(self):
        return self.__id

    @id.setter
    def set_id(self):
        raise NotImplemented
