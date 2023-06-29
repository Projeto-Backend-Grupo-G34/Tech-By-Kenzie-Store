from django.db import models
from carts.models import Cart
from orders.models import Order
from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=25)
    quantity = models.IntegerField()
    price = models.IntegerField()

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="product"
    )

    orders = models.ManyToManyField(
        Order,
        related_name="product",
    )

    carts = models.ManyToManyField(
        Cart,
        related_name="product",
    )
