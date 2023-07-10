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

        fields = ["id", "status", "created_at", "user", "items"]

    def update(self, instance, validated_data):
        status = validated_data.get("status")
        if status:
            instance.status = status
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
