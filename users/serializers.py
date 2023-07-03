from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from addresses.serializers import AddressSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "is_employee",
            "is_superuser",
            "address",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict):
        address_data = validated_data.pop("address")
        password = validated_data.pop("password")
        validated_data["password"] = make_password(password)
        address = AddressSerializer.create(
            AddressSerializer(), validated_data=address_data
        )
        user = self.Meta.model.objects.create_user(**validated_data)
        user.address = address
        user.save()
        return user

    def update(self, instance: User, validated_data: dict):
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.password = make_password(password)
        address_data = validated_data.pop("address", None)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        if address_data is not None:
            address_serializer = AddressSerializer(instance.address, data=address_data)
            if address_serializer.is_valid():
                address_serializer.save()
        instance.save()
        return instance
