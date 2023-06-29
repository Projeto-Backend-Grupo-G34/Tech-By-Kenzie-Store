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
        related_name="user"
    )

    orders = models.ManyToManyField(
        Order,
        on_delete=models.CASCADE,
        related_name="orders",
    )

    carts = models.ManyToManyField(
        Cart,
        on_delete=models.CASCADE,
        related_name="carts",
    )
