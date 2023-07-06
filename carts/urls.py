from django.urls import path

from .views import CartAddView, CartCheckoutView, CartView

urlpatterns = [
    path("cart/", CartView.as_view()),
    path("cart/add_product/", CartAddView.as_view()),
    path("cart/checkout/", CartCheckoutView.as_view()),
]
