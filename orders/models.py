from django.db import models
from users.models import User


class Status(models.TextChoices):
    PEDIDO_REALIZADO = "Pedido realizado"
    EM_AMDAMENTO = "Em andamento"
    ENTREGUE = "Entregue"


class Order(models.Model):
    status = models.CharField(max_length=50, 
        choices=Status.choices, default=Status.EM_AMDAMENTO,
    )
    buyed_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="order"
    )
