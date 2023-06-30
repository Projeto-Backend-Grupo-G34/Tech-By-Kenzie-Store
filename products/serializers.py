from rest_framework import serializers
from products.models import Product
from users.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model: Product
        fields = [
            "id",
            "name",
            "quantity",
            "price"
        ]
