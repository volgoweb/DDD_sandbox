from orchestrator.repository_registers import IRepositoryRegistry, ConfigFileRepositoryRegistry


class RepositoryRegister(ConfigFileRepositoryRegistry):
    # @TODO перенести в app.settings
    _map = {
        'carts': 'carts.repositories.base.CartsRepo'
    }


repository_register = RepositoryRegister()
