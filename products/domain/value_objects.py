from django.utils.translation import ugettext_lazy as l_


class Price(object):
    def __init__(self, id_: int, currency: Currency, type: PriceType):
        pass


class Currency(object):
    CODE_RUB = 'rub'
    CODE_NAME_MAP = {
        CODE_RUB: l_('Ruble'),
    }

    def __init__(self, code: str):
        raise code in self.available_codes
        self.code = code
        self.name = self.get_name_by_code(code)

    @property
    def available_codes(self):
        return list(self.CODE_NAME_MAP.keys())

    def get_name_by_code(self, code: str):
        return self.CODE_NAME_MAP[code]
