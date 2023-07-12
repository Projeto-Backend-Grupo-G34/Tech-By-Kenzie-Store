from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from orders.models import Order
from orders.serializers import OrderSerializer
from users.permissions import IsInstanceOrAdmin, IsVendorOrAdmin, IsVendorOrAdminForGet


class OrderView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = OrderSerializer
    permission_classes = [IsVendorOrAdminForGet]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(products__vendor=user)

    @extend_schema(
        operation_id="order_list",
        description="List sold orders",
        summary="List Sold Orders",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserOrderView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = OrderSerializer
    permission_classes = [IsInstanceOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(user=user)

    @extend_schema(
        operation_id="order_list",
        description="List purchased oders",
        summary="List Purchased Orders",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsVendorOrAdmin]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @extend_schema(
        operation_id="order_retrieve",
        description="Retrieve an order by ID",
        summary="Retrieve Order",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        operation_id="order_put",
        description="Update an order by ID",
        summary="Update Order",
        exclude=True,
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        operation_id="order_patch",
        description="Partially update an order by ID",
        summary="Update Order",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        operation_id="order_delete",
        description="Delete an order by ID",
        summary="Delete Order",
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
