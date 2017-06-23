from django.db import models


class Cart(models.Model):
    user_id = models.IntegerField(unique=True)


class CartItem(models.Model):
    cart_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.PositiveSmallIntegerField(default=0, blank=True)
    price = models.DecimalField(blank=True, null=True)
