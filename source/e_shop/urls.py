from django.urls import path

from .views import products_view

urlpatterns = [
    path("", products_view, name="products_view"),
    path("products/", products_view, name="products_view"),
]