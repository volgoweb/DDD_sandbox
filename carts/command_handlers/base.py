from ..repositories.register import RepositoryRegister
from ..domain.entities import CartItem
from orchestrator.command_handler_registers import ICommandHandler
#
# api.command_dispatcher -> Pick up Command Handler -> CommandHandler(**kwargs)
#
# settings.command_handler_map = {
#     AddToCart.TYPE: 'cart.AddToCartHandler',
# }
# settings.repository_map = {
#     ICartRepository: PostgresCartRepository
#     IProductRepository: PostgresCartRepository
# }
#
# class CommandType(str):
#     def __init__(self, type_name):
#         self._type_name = type_name
#
#     def __str__(self):
#         return self._type_name
#
#
#
# class CommandDispatcher(object):
#     _handlers_map = {}
#
#     @classmethod
#     def register(cls, command_cls, handler_cls):
#         cls._handlers_map[command_cls.TYPE] = handler_cls
#
#     def dispatch(self, command):
#         handler_cls = self.get_handler_cls(command.TYPE)
#         handler = handler_cls()
#         handler.handle(command)
#
#     @classmethod
#     def get_handler(cls, command_type):
#         try:
#             h = cls._handlers_map[command_type]
#             return h
#         except IndexError:
#             raise HandlerNotFound()
#
#
# CommandDispatcher.register(AddToCart, AddToCartHandler)
#
#
# class HandlerFactory(object):
#
#
#
#
#
class AddToCartHandler(ICommandHandler):
    def __init__(self):
        self.cart_repository = RepositoryRegister().get('CartRepository')
        self.item_entity = CartItem
        # self.prices_adapter = prices_adapter

    def handle(self, command):
        cart = self.cart_repository.get_by_user_id(command.user_id)
        item = self.item_entity(
            product_id=command.product_id,
            quantity=command.quantity,
            # price=self.get_price(command.product_id, command.user_id),
        )
        cart.add_item(item)
        self.cart_repository.save_one(cart)

    # def get_price(self, product_id, user_id):
    #     spec = ProductPriceQuerySpec()
    #     prices_adapter.query_request(spec)
