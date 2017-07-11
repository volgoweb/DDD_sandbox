import json
import jsonschema
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


def execute_json_command(msg_json: str):
    msg = MessageParser().parse(msg_json)
    command = msg['body']
    handler_cls = command_handler_register.get(command)
    handler = handler_cls()
    # @TODO Вообще-то команда не должна возвращать результат. Но пока я отложил этот вопрос.
    result = handler.handle(command)
    return result


MSG_SCHEMA = {
    '$schema': 'message',
    'type': 'object',
    'properties': {
        'message_type': {
            'type': 'string',
            'enum': ['command', 'query'],
        },
        'created': {
            'type': 'string',
            'pattern': '^\d{4}-[01]\d-[01]\d\s[012]\d:\d{2}:\d{2}$',
        },
        'body': {
            'type': 'object',
        },
    },
    'required': [
        'message_type',
        'created',
        'body',
    ],
}


COMMAND_BODY_SCHEMA_EXAMPLE = {
    '$schema': 'command_add_to_cart',
    'type': 'object',
    'properties': {
        'user_id': {
            'type': 'number',
        },
        'product_id': {
            'type': 'number',
        },
    },
    'required': [
        'user_id',
        'product_id',
    ],
}


class MessageParser(object):
    def __init__(self):
        self.msg_schema = MSG_SCHEMA

    def parse(self, msg_json):
        msg = json.loads(msg_json)
        jsonschema.validate(msg, self.msg_schema)
        msg_body_schema = self.get_msg_body_schema(msg['type'])
        jsonschema.validate(msg['body'], msg_body_schema)
        return msg

    def get_msg_body_schema(self, msg_type):
        return COMMAND_BODY_SCHEMA_EXAMPLE
