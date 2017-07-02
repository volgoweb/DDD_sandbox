from django.utils.module_loading import import_string


class ICommandHandler(object):
    def handle(self, command):
        raise NotImplementedError


class CommandHandlerRegister(object):
    # @TODO Перенести в settings
    _map = {
        'carts.AddToCart': 'carts.command_handlers.base.AddToCartHandler',
    }

    def get(self, command):
        command_type = command.get_command_type_name()
        path = self._map[command_type]
        handler = import_string(path)
        return handler

        # from carts.command_handlers.base import AddToCartHandler
        # return AddToCartHandler


command_handler_register = CommandHandlerRegister()


def execute_command(command):
    handler_cls = command_handler_register.get(command)
    handler = handler_cls()
    # @TODO Вообще-то команда не должна возвращать результат. Но пока я отложил этот вопрос.
    result = handler.handle(command)
    return result
