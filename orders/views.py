from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication

from orders.models import Order
from orders.serializers import OrderSerializer
from users.permissions import IsSellerOrAdmin, IsVendorOrAdmin


class OrderView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = OrderSerializer
    permission_classes = [IsSellerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(products__vendor=user)


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsVendorOrAdmin]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
