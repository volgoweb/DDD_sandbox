from orchestrator.repository_registers import IRepositoryRegistry, ConfigFileRepositoryRegistry


class RepositoryRegister(ConfigFileRepositoryRegistry):
    # @TODO перенести в app.settings
    _map = {
        'CartRepository': 'carts.repositories.base.CartRepository'
    }


repository_register = RepositoryRegister()
