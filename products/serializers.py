from rest_framework import serializers

from users.models import User
from users.serializers import UserSerializer

from .models import Product


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class ProductSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "category", "description", "price", "stock", "vendor"]

    def create(self, validated_data: dict):
        user = self.context.get("request").user
        validated_data["vendor"] = user
        return Product.objects.create(**validated_data)
