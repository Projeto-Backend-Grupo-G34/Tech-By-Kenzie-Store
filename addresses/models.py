from django.db import models
from users.models import User


class Address(models.Model):
    street = models.CharField(max_length=150)
    number = models.IntegerField()
