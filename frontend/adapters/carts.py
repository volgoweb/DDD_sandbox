from carts.api.commands import AddToCart


def add_to_cart(user_id, product_modification_id):
    command = AddToCart(user_id, product_modification_id)
    command.execute()
