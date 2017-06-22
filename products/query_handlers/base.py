from ..repositories.register import repository_register


class AllProducts(object):
    def __init__(self):
        repo_cls = repository_register.get('ProductsRepository')
        self.products_repo = repo_cls()

    def execute(self, query):
        return self.products_repo.all()
