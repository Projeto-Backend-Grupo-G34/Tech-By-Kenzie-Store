from rest_framework import serializers

from users.serializers import UserSerializer

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    vendor = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ["name", "category", "description", "price", "stock", "vendor"]
