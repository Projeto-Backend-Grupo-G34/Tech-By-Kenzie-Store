from rest_framework import serializers
from addresses.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "street",
            "number",
            "zip_code",
        ]

    def create(self, validated_data: dict):
        address_data = Address.objects.create(**validated_data)
        validated_data["user"].address = address_data
        validated_data["user"].save()
        return address_data

    def update(self, instance: Address, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance