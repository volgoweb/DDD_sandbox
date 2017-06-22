from orchestrator.repository_registers import ConfigFileRepositoryRegistry


class RepositoryRegister(ConfigFileRepositoryRegistry):
    # @TODO перенести в app.settings
    _map = {
        'ProductsRepository': 'products.repositories.base.ProductsRepository'
    }


repository_register = RepositoryRegister()
