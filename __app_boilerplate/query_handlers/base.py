from ..repositories.register import repository_register


class SomeQueryHandler(object):
    def __init__(self):
        repo_cls = repository_register.get('SomeRepository')
        self.repo = repo_cls()

    def execute(self, query):
        return self.repo.all()
