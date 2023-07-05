from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=150)
    number = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=8)
