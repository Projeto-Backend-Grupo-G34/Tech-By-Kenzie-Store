from rest_framework import serializers
from carts.models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model: Cart
        fields = [
            "id",
            "quantity",
            "total_price",
        ]
