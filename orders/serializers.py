from rest_framework import serializers

from products.serializers import ProductSerializer
from users.serializers import UserSerializer

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
        return instance

    def delete(self, instance):
        if instance.status != Order.Status.ENTREGUE:
            raise serializers.ValidationError("Pedido ainda não foi entregue")
        instance.delete()
