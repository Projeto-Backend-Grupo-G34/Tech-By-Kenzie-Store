from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from users.models import User
from addresses.serializers import AddressSerializer

class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "cpf",
            "password",
            "is_employee",
            "is_superuser",
            "address",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict):
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict):
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.password = make_password(password)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
