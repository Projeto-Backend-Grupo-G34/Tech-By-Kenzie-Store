from django.urls import path
from .views import OrderDetailView, OrderView

urlpatterns = [
    path("orders/", OrderView.as_view()),
    path("orders/<int:pk>/", OrderDetailView.as_view()),
]
