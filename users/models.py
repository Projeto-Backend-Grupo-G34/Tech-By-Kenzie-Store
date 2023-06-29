from django.db import models
from django.contrib.auth.models import AbstractUser
from addresses.models import Address
from carts.models import Cart


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=127, unique=True)
    is_employee = models.BooleanField(default=False, null=True)
    is_superuser = models.BooleanField(default=False, null=True)

    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        related_name="address",
    )

    cart = models.OneToOneField(
        Cart,
        on_delete=models.PROTECT,
        related_name="cart"
    )
