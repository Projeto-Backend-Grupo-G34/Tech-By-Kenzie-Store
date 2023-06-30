from rest_framework import serializers
from orders.models import Order
from users.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model: Order
        fields = [
            "id",
            "status",
            "buyed_at",
        ]
