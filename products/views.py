from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.permissions import IsOwnerOrAdmin, IsVendorOrAdmin, IsVendorOrAdminForPost

from .models import Product
from .serializers import ProductSerializer


class ProductView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsVendorOrAdminForPost]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrAdmin]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"
