from orchestrator.repository_registers import ConfigFileRepositoryRegistry


class RepositoryRegister(ConfigFileRepositoryRegistry):
    # @TODO перенести в app.settings
    _map = {
        '': ''
    }


repository_register = RepositoryRegister()
