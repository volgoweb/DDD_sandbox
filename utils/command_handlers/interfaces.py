from ..commands.interfaces import ICommand


class ICommandHandler(object):
    def handle(self, command: ICommand):
        raise NotImplementedError