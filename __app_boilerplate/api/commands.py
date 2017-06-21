from utils.commands import ICommand


class SomeCommand(ICommand):
    def execute(self, param1: int, param2: str) -> None:
        return None
