from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from carts.serializers import CartCheckoutSerializer, CartItemSerializer, CartSerializer
from users.permissions import IsOwnerOrAdmin
from .models import Cart
from drf_spectacular.utils import extend_schema


class CartView(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        return Cart.objects.filter(user_id=user_id)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj
    
    @extend_schema(
        operation_id="cart_retrieve",
        description="Retrieve cart details by ID",
        summary="Retrieve Cart",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CartAddView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = CartItemSerializer
    permission_classes = [IsOwnerOrAdmin]

    @extend_schema(
        operation_id="cart_post",
        description="Add Product to Cart by ID",
        summary="Add Product to Cart",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CartCheckoutView(CreateAPIView):
    serializer_class = CartCheckoutSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def perform_create(self, serializer):
        return serializer.save()
    
    @extend_schema(
        operation_id="cart_checkout",
        description="Checkout the Cart",
        summary="Checkout Cart",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
