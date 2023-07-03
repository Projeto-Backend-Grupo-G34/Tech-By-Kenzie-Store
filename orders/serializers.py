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
    items = OrderItemSerializer(source="items", many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["status", "created_at", "user", "items"]
