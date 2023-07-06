from rest_framework.views import APIView, Request, Response, status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from orders.models import Order
from orders.serializers import OrderSerializer


class OrderView(APIView):
    ...


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
