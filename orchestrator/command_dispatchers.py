# from django.conf import settings
# from django.utils.module_loading import import_string
#
# from utils.command_handlers.interfaces import ICommandHandler
# from utils.commands.interfaces import ICommand
# from .repository_dispatchers import get_repository_dispatcher
#
#
# def execute_command(command: ICommand):
#     handler = settings.command_handler_map[command.TYPE_NAME]
#     repo_dispatcher = get_repository_dispatcher()
#     repository_dispatcher = settings.repository_dispatcher
#     handler(repo_dispatcher)
#
#
#     hd = get_command_handler_dispatcher()
#     repo_dispatcher = get_repository_dispatcher()
#     handler = handlers_dispatcher(repo_dispatcher)
#     handler.execute(command)
#
# def get_handler_dispatcher():
#     return CommandHandlerDispatcher()
#
# class CommandHandlerDispatcher(object):
#     def get_handler(self, command):
#         repo_dispatcher = get_repository_dispatcher()
#         handler_cls = settings.handlers_map.get(command)
#         return handler_cls(repo_dispatcher)
#
#     def handle(self):
#
# def get_handler(command):
#
#
#
# class CommandHandlerFactory(object):
#     def create(self, command):
#         repo_dispatcher = get_repository_dispatcher()
#         handler_cls = settings.handlers_map.get(command)
#         return handler_cls(repo_dispatcher)
#

