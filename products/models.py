from django.db import models

from users.models import User


class CategoryChoices(models.TextChoices):
    XBOX = "XBOX"
    PLAYSTATION = "PLAYSTATION"
    PC = "PC"
    DEFAULT = "INDEFINIDO"


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(
        max_length=12, choices=CategoryChoices.choices, default=CategoryChoices.DEFAULT
    )
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
