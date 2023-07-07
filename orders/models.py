from django.db import models

from products.models import Product
from users.models import User


class Status(models.TextChoices):
    PEDIDO_REALIZADO = "Pedido realizado"
    EM_ANDAMENTO = "Em andamento"
    ENTREGUE = "Entregue"


class Order(models.Model):
    status = models.CharField(
        max_length=50,
        choices=Status.choices,
        default=Status.PEDIDO_REALIZADO,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order")
    products = models.ManyToManyField(
        Product, through="OrderItem", related_name="orders"
    )


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="items")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
