from rest_framework import serializers

from products.serializers import ProductSerializer
from users.serializers import UserSerializer
from django.core.mail import send_mail
from django.conf import settings
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ["product", "quantity", "price"]


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["status", "created_at", "user", "items"]

    def update(self, instance: Order, validated_data: dict) -> Order:
        new_status = validated_data.get("status")

        if new_status == instance.status:
            return instance

        if instance.status == Order.Status.ENTREGUE:
            raise serializers.ValidationError("Pedido entregue")

        if (
            instance.status == Order.Status.EM_ANDAMENTO
            and new_status == Order.Status.PEDIDO_REALIZADO
        ):
            instance.status = new_status
        elif (
            instance.status == Order.Status.PEDIDO_REALIZADO
            and new_status == Order.Status.ENTREGUE
        ):
            instance.status = new_status

        instance.save()

        send_mail(
            subject="Atualização de Pedido - Tech By Kenzie",
            message=f"O status do seu pedido foi atualizado para: {instance.get_status_display()}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[instance.user.email],
            fail_silently=False,
        )

        return instance

    def delete(self, instance):
        if instance.status != Order.Status.ENTREGUE:
            raise serializers.ValidationError("Pedido ainda não foi entregue")
        instance.delete()
