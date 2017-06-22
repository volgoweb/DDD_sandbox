from django.utils.module_loading import import_string


class ICommandHandler(object):
    def handle(self, command):
        raise NotImplementedError


class CommandHandlerRegister(object):
    # @TODO Перенести в settings
    _map = {
        'carts.AddToCart': 'carts.command_handlers.base.AddToCartHandler',
    }

    def get(self, query):
        # query_type = query.get_query_type_name()
        # path = self._map[query_type]
        # handler = import_string(path)
        # return handler
        from carts.command_handlers.base import AddToCartHandler
        return AddToCartHandler


command_handler_register = CommandHandlerRegister()
