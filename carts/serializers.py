from rest_framework import serializers
from products.models import Product
from products.serializers import ProductSerializer
from users.serializers import UserSerializer
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ["product", "quantity"]


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
