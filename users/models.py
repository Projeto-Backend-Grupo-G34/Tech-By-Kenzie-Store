from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        ordering = ["id"]

    username = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=127, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    is_employee = models.BooleanField(default=False, null=True)
    is_superuser = models.BooleanField(default=False, null=True)
