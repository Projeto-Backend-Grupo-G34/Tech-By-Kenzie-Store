from django.db import models
from users.models import User


class Cart(models.Model):
    quantity = models.IntegerField()
    total_price = models.IntegerField()
