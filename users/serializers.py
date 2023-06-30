from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from addresses.serializers import AddressSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)
    class Meta:
        model = User
        fields = [
            "id", 
            "username", 
            "email", 
            "password",
            "is_employee",
            "is_superuser",
            "address",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_employee": {"required": False},
            "is_superuser": {"required": False},
        }

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
