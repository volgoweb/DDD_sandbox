from carts.api.commands import AddToCart
from carts.api.queries import CartOfUserQuery
from orchestrator.command_handler_registers import execute_command
from orchestrator.query_handler_registers import send_query


def add_to_cart(user_id: int, product_id: int, quantity=None):
    command = AddToCart(user_id, product_id, quantity)
    execute_command(command)


def get_cart(user_id):
    q = CartOfUserQuery(user_id)
    result = send_query(q)
    return result