from django.db import models


class Cart(models.Model):
    user_id = models.IntegerField(unique=True)


class CartItem(models.Model):
    cart_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.PositiveSmallIntegerField(default=0, blank=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        unique_together = ['cart_id', 'product_id']
