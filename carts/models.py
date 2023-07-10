from django.db import models
from products.models import Product
from users.models import User


class Cart(models.Model):
    products = models.ManyToManyField(Product, through="CartItem", related_name="cart")
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="cart")


class CartItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="cart_items"
    )
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.IntegerField()
