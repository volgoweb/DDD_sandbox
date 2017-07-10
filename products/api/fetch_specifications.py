class SupplierProductsSpecification(object):
    def __init__(self, supplier_id):
        self.supplier_id = supplier_id

    def filter(self, qs):
        qs.filter(supplier=self.supplier_id)
        return qs


class PublishedProductsSpecification(object):
    def filter(self, qs):
        qs.filter(published=True)
        return qs


class ProductsWithNotNullPriceSpecification(object):
    def filter(self, qs):
        qs.filter(price__isnull=False)
        return qs




"""
Список активных товаров

Подробно о товаре

Товары из категории

Товары поставщика из категории для каталога
filter(supplier, category).only(catalog_fields)

Товары по цене для каталога
filter(price).only(catalog_fields)

"""


class IFetchSpecification(object):
    def fetch(self, qs):
        raise NotImplementedError


class ProductCatalogItemFetch(IFetchSpecification):
    def fetch(self, qs):
        values = qs.values('id', 'name', 'description', 'image')
        return values


class ProductsAutocompleteFetch(IFetchSpecification):
    def fetch(self, qs):
        values = qs.values('id', 'name')
        return values


class BaseQueryHandler(object):
    base_queryset = None

    # def __init__(self, filter_specifications=None, fetch_specification=None):
    #     self.filter_specifications = filter_specifications
    #     self.fetch_specification = fetch_specification

    def __init__(self, query):
        self.query = query
        self.filter_specifications

    def handle(self):
        qs = self.base_queryset
        for fs in self.query.filter_specifications:
            qs = fs.filter(qs)

        rows = self.query.fetch_specification.fetch(qs)
        return rows


class QHProducts(BaseQueryHandler):
    base_queryset = Product.objects.all()


"""
query = SupplierProductsQuery(supplier_id)
dto = send_query(query)
"""


class SupplierProductsQuery(object):
    def __init__(self, supplier_id):
        self.filter_specifications = [
            SupplierProductsSpecification(supplier_id),
            PublishedProductsSpecification(),
            ProductsWithNotNullPriceSpecification(),
        ]
        self.fetch_specification = ProductCatalogItemFetch()


class SupplierProductsAutocompleteQuery(SupplierProductsQuery):
    def __init__(self, supplier_id):
        super(SupplierProductsAutocompleteQuery, self).__init__(supplier_id)
        self.fetch_specification = ProductsAutocompleteFetch()


class ConverterORMToDTO(object):
    def convert(self, row):
        dto = row.deep_copy()
        # для некоторых полей может быть переопределение
        return dto

class SupplierProductsAutocompleteDTO():
    pass


class ISupProductsFilterSpec():
    def __init__(self, sid):
        pass

class Sup(ISupProductsFilterSpec):
    def filter(self, qs):
        qs.filter(supplier=self.supplier_id)
        return qs


