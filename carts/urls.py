from django.urls import path
from .views import CartAddView, CartCheckoutView, CartView

urlpatterns = [
    path("cart/<int:user_id>/", CartView.as_view()),
    path("cart/<int:user_id>/add_product", CartAddView.as_view()),
    path("cart/<int:user_id>/checkout", CartCheckoutView.as_view()),
]
