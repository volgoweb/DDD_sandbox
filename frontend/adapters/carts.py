from sales.carts.api.v_1_0.commands import AddToCart


def add_to_cart(user_id, product_modification_id):
    command = AddToCart(user_id, product_modification_id)
    command.execute()
