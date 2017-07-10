from orchestrator.repository_registers import ConfigFileRepositoryRegistry


class RepositoryRegister(ConfigFileRepositoryRegistry):
    # @TODO перенести в app.settings
    _map = {
        'PriceType': 'prices.repositories.dummy.DummyPriceTypeRepo',
        'Currency': 'prices.repositories.dummy.DummyCurrencyRepo',
        'ProductPricing': 'prices.repositories.dummy.DummyProductPricingRepo',
    }


repository_register = RepositoryRegister()
