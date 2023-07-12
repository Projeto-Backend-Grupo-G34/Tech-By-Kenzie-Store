from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.permissions import IsOwnerOrAdmin, IsVendorOrAdminForPost

from .models import Product
from .serializers import ProductSerializer


class ProductView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsVendorOrAdminForPost]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ["category", "name", "id"]

    @extend_schema(
        operation_id="product_list",
        description="List products",
        summary="List Products",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        operation_id="product_create",
        description="Create a new product",
        summary="Create Product",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrAdmin]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

    @extend_schema(
        operation_id="product_retrieve",
        description="Retrieve a product by ID",
        summary="Retrieve Product",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        operation_id="product_put",
        description="Update a product by ID",
        summary="Update Product",
        exclude=True,
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        operation_id="product_patch",
        description="Partially update a product by ID",
        summary="Update Product",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        operation_id="product_delete",
        description="Delete a product by ID",
        summary="Delete Product",
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
