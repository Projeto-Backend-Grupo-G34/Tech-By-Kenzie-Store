from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from carts.models import Cart
from carts.serializers import CartItemSerializer, CartSerializer
from products.models import Product
from users.models import User
from rest_framework.exceptions import NotFound


class CartView(RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Cart.objects.filter(user_id=user_id)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj


class CartAddView(CreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Cart.objects.filter(user_id=user_id)

    def perform_create(self, serializer):
        user_id = self.kwargs.get("user_id")
        user = get_object_or_404(User, id=user_id)

        product_name = self.request.data.get("product")

        try:
            product = Product.objects.get(name=product_name)
        except Product.DoesNotExist:
            raise NotFound(detail="Product not found")

        serializer.save(user=user, product=product)


class CartCheckoutView(UpdateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Cart.objects.filter(user_id=user_id)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj

    def update(self, request, *args, **kwargs):
        cart = self.get_object()
        cart.is_checked_out = True
        cart.save()
        serializer = self.get_serializer(cart)
        return Response(serializer.data)
