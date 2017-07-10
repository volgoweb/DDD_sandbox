from ..repositories.register import RepositoryRegister
from orchestrator.command_handler_registers import ICommandHandler


class SomeHandler(ICommandHandler):
    def __init__(self):
        self.cart_repository = RepositoryRegister().get('SomeRepository')

    def handle(self, command):
        pass
