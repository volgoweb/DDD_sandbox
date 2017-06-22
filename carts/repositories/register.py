from orchestrator.repository_registers import IRepositoryRegistry, ConfigFileRepositoryRegistry


class RepositoryRegister(ConfigFileRepositoryRegistry):
    # @TODO перенести в app.settings
    _map = {
        'CartRepository': 'products.repositories.ProductRepository'
    }


repository_register = RepositoryRegister()
