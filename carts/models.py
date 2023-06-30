from django.db import models


class Cart(models.Model):
    quantity = models.IntegerField()
    total_price = models.IntegerField()
