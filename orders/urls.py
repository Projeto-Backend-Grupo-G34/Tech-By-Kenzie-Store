from django.urls import path

from .views import OrderDetailView, OrderView, UserOrderView

urlpatterns = [
    path("orders/", UserOrderView.as_view()),
    path("orders/sold/", OrderView.as_view()),
    path("orders/<int:pk>/", OrderDetailView.as_view()),
]
