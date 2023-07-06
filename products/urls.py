from django.urls import path
from .views import ProductDetailView, ProductView

urlpatterns = [
    path("products/", ProductView.as_view()),
    path("products/<int:id>", ProductDetailView.as_view()),
]
