from django.db import models
from users.models import User


class Address(models.Model):
    class Meta:
        ordering = ["id"]

    street = models.CharField(max_length=150)
    number = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=8)

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="address",
    )
