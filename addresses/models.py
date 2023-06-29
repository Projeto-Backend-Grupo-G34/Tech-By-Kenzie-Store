from django.db import models



class Address(models.Model):
    street = models.CharField(max_length=150)
    number = models.IntegerField()

