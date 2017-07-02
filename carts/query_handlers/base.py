from collections import namedtuple

from orchestrator.query_handler_registers import IQueryHandler
from ..repositories.register import RepositoryRegister
from ..domain.entities import CartItemEntity
from ..domain.aggregates import CartAggregate
from ..repositories.register import repository_register
from ..exceptions import UserDoesNotHaveCart
from ..domain.services.cart_processors import AddProductNameIntoCartItems


class CartOfUser(IQueryHandler):
    def __init__(self):
        repo_cls = repository_register.get('carts')
        self.carts_repo = repo_cls()
        self.cart_processors = [AddProductNameIntoCartItems]

    @staticmethod
    def get_query_type_name():
        return 'carts.CartOfUser'

    def handle(self, query):
        try:
            cart = self.carts_repo.get_by_user_id(query.user_id)
        except UserDoesNotHaveCart:
            # @TODO куда-то вынести (в сервис или еще куда)
            cart = CartAggregate(user_id=query.user_id)
            self.carts_repo.add_one(cart)
            cart = self.carts_repo.get_by_user_id(query.user_id)

        for proc_cls in self.cart_processors:
            proc = proc_cls()
            proc.run(cart)

        # @TODO вставить конвертацию в DTO
        cart_DTO = dict(
            id=cart.id,
            user_id=cart.user_id,
            items=[],
        )

        for item in cart.items:
            idto = dict(
                id=item.id,
                product_id=item.product_id,
                product_name=item.product_name,
                quantity=item.quantity,
            )
            cart_DTO['items'].append(idto)
        return cart_DTO
