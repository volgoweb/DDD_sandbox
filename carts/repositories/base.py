from ..domain.aggregates import CartAggregate
from ..domain.entities import CartItemEntity
from ..domain.repository_interfaces import ICartsRepo
from ..models import Cart, CartItem
from ..exceptions import UserDoesNotHaveCart

# @TODO Подумать, может репозиторий заставить отдавать DTO, а в слое домена DTO преобразовывать в сущности (может через фабрики)

class CartsRepo(ICartsRepo):
    def get_by_user_id(self, user_id: int):
        # @TODO добавить auto mapper
        try:
            cart_model = Cart.objects.get(user_id=user_id)
        except Cart.DoesNotExist:
            raise UserDoesNotHaveCart
        cart = CartAggregate(
            _id=cart_model.pk,
            user_id=cart_model.user_id,
        )
        items_models = CartItem.objects.filter(cart_id=cart_model.pk)
        for im in items_models:
            item = CartItemEntity(
                product_id=im.product_id,
                quantity=im.quantity,
                _id=im.pk,
            )
            cart.add_item(item)
        return cart

    def add_one(self, cart):
        if self.does_user_have_cart(cart.user_id):
            # @TODO добавить свое исключение
            raise ValueError
        cart_model = Cart.objects.create(
            user_id=cart.user_id,
        )
        for item in cart.items:
            CartItem.objects.create(
                cart_id=cart_model.pk,
                product_id=item.product_id,
                quantity=item.quantity,
            )

    def does_user_have_cart(self, user_id: int):
        # @TODO создать для модели queryset и manager
        user_has_cart = Cart.objects.filter(user_id=user_id).exists()
        return user_has_cart

    def update(self, cart):
        cart_model = Cart.objects.get(pk=cart.id)
        items_ids = []
        for item in cart.items:
            item_model, created = CartItem.objects.get_or_create(pk=item.id, defaults={
                'cart_id': cart_model.pk,
                'product_id': item.product_id,
            })
            item_model.quantity = item.quantity
            item_model.save()
            items_ids.append(item.id)
        CartItem.objects.filter(cart_id=cart.id).exclude(pk__in=items_ids).delete()

    def delete(self, cart):
        pass

