from django.conf import settings

from ..command_handlers.interfaces import ICommandHandler
from ..commands.interfaces import ICommand

def execute_command(command: ICommand):
    handler = settings.command_handler_map[command.TYPE_NAME]
    handler.execute(command)

# def get_command_handler_dispatcher():
#     return CommandHandlerDispatcherFromConfig()
#
#
# class ICommandHandlerConfig(object):
#     def get(self, command_type_name: str)-> ICommandHandler:
#         raise NotImplementedError
#
#
# class CommandHandlerConfigFromFile(ICommandHandlerConfig):
#     def get(self, command_type_name: str):
#         h = settings.command_handler_map[command_type_name]
#         return h
#
#
# class CommandHandlerConfigFromDB(ICommandHandlerConfig):
#     def get(self, command_type_name: str):
#         # h = getting from database
#         # return h
#         pass
