from rest_framework import serializers

from products.serializers import ProductSerializer
from users.serializers import UserSerializer

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ["product", "quantity", "price"]


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    items = OrderItemSerializer(source="items", many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["status", "created_at", "user", "items"]

    # def create(self, validated_data: dict) -> Order:
    #     ...

    def update(self, instance: Order, validated_data: dict) -> Order:
        new_status = validated_data.get("status")

        if new_status == instance.status:
            return instance

        if instance.status == Order.Status.ENTREGUE:
            raise serializers.ValidationError("Pedido entregue")

        if (
            instance.status == Order.Status.EM_ANDAMENTO
            and new_status == Order.Status.PEDIDO_REALIZADO
        ):
            instance.status = new_status
        elif (
            instance.status == Order.Status.PEDIDO_REALIZADO
            and new_status == Order.Status.ENTREGUE
        ):
            instance.status = new_status

        instance.save()
        return instance

    def delete(self, instance):
        if instance.status != Order.Status.ENTREGUE:
            raise serializers.ValidationError("Pedido ainda não foi entregue")
        instance.delete()
