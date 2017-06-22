from django.utils.module_loading import import_string


class IRepositoryRegistry(object):
    def get(self, name):
        raise NotImplementedError


class ConfigFileRepositoryRegistry(IRepositoryRegistry):
    # # @TODO перенести в app.settings
    # _map = {
    #     'ProductsRepository': 'products.repositories.base.ProductsRepository'
    # }

    def get(self, name):
        repo_path = self._map[name]
        repo = import_string(repo_path)
        return repo
