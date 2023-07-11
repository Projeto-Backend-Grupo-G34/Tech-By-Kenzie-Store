from django.conf import settings
from django.core.mail import send_mail
from django.db.models import F
from rest_framework import serializers
from orders.models import Order, OrderItem
from products.models import Product
from users.serializers import UserSerializer
from .models import Cart, CartItem
from rest_framework.exceptions import NotFound


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

    def get_object_or_404(self):
        user_id = self.context["request"].user.id
        queryset = Cart.objects.filter(user_id=user_id)
        if not queryset.exists():
            raise NotFound("Cart not found.")
        return queryset.first()
    
    def get(self, request, *args, **kwargs):
        instance = self.get_object_or_404()
        serializer = self.retrieve(instance)
        return serializer


class CartCheckoutSerializer(serializers.Serializer):
    def create(self, validated_data):
        user = self.context["request"].user

        if not user.is_authenticated:
            raise serializers.ValidationError("Usuário não autenticado")

        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            raise serializers.ValidationError("Carrinho vazio")

        if cart.cart_items.count() == 0:
            raise serializers.ValidationError("Carrinho vazio")

        vendors = set([item.product.vendor for item in cart.cart_items.all()])
        if len(vendors) > 1:
            orders = []
            for vendor in vendors:
                order = Order.objects.create(user=user)
                order_items = cart.cart_items.filter(product__vendor=vendor)
                for item in order_items:
                    OrderItem.objects.create(
                        order=order,
                        product=item.product,
                        quantity=item.quantity,
                        price=item.product.price,
                    )
                orders.append(order)
            cart.cart_items.all().delete()

            for order in orders:
                send_mail(
                    subject="Pedido - Tech By Kenzie",
                    message="Seu pedido foi realizado.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[user.email],
                    fail_silently=False,
                )

            return orders
        else:
            order = Order.objects.create(user=user)
            for item in cart.cart_items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price,
                )
            cart.cart_items.all().delete()

            send_mail(
                subject="Pedido - Tech By Kenzie",
                message="Seu pedido foi realizado.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
            )

            return order
