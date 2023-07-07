from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication

from carts.serializers import CartCheckoutSerializer, CartItemSerializer, CartSerializer
from orders.models import Order, OrderItem
from orders.serializers import OrderSerializer
from products.models import Product
from users.models import User
from users.permissions import IsOwnerOrAdmin

from .models import Cart, CartItem


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
    authentication_classes = [JWTAuthentication]
    serializer_class = CartItemSerializer
    permission_classes = [IsOwnerOrAdmin]


class CartCheckoutView(CreateAPIView):
    serializer_class = CartCheckoutSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def perform_create(self, serializer):
        return serializer.save()
