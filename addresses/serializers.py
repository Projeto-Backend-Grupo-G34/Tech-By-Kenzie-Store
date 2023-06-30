from rest_framework import serializers
from addresses.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "street"
            "number"
        ]

    def create(self, validated_data: dict):
        return Address.objects.create(**validated_data)