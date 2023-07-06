from django.db.models import F
from rest_framework import serializers

from products.models import Product
from products.serializers import ProductSerializer
from users.serializers import UserSerializer

from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["product", "quantity"]

    def create(self, validated_data: dict):
        user = self.context["request"].user
        product = validated_data["product"]
        quantity = validated_data["quantity"]

        if user.is_anonymous:
            raise serializers.ValidationError("User is not logged in")
        if product.stock == 0:
            raise serializers.ValidationError("Product is out of stock")
        elif quantity > product.stock:
            raise serializers.ValidationError("Quantity is greater than stock")

        product.stock = product.stock - quantity
        product.save()

        cart, created = Cart.objects.get_or_create(user=user)
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product, quantity=quantity
        )
        if not created:
            CartItem.objects.filter(cart=cart, product=product).update(
                quantity=F("quantity") + quantity
            )

        return cart_item


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    cart_items = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["user", "cart_items"]

    def get_cart_items(self, obj):
        cart_items = CartItem.objects.filter(cart=obj)
        serializer = CartItemSerializer(cart_items, many=True)
        return serializer.data

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user

        cart = Cart.objects.create(user=user)
        cart_items_data = validated_data.get("cart_items")

        for item_data in cart_items_data:
            product_data = item_data.get("product")
            quantity = item_data.get("quantity")
            product = Product.objects.get(pk=product_data["id"])
            CartItem.objects.create(cart=cart, product=product, quantity=quantity)

        return cart

    def retrieve(self, instance):
        return instance
