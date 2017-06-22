from carts.api.commands import AddToCart
# from orchestrator.command_dispatchers import execute_command


def add_to_cart(user_id, product_modification_id):
    command = AddToCart(user_id, product_modification_id)
    # execute_command(command)
