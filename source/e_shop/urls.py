from django.urls import path

from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    CategoryCreateView,
    CartView,
    CartAddView,
    CartDeleteView,
)

urlpatterns = [
    path("", ProductListView.as_view(), name="products_view"),
    path("products/", ProductListView.as_view(), name="products_list"),
    path("products/add/", ProductCreateView.as_view(), name="product_add_view"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_view"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update_view"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete_view"),
    path("categories/add/", CategoryCreateView.as_view(), name="category_add_view"),
    path("cart/", CartView.as_view(), name="cart_view"),
    path("cart/add/<int:pk>/", CartAddView.as_view(), name="cart_add"),
    path("cart/delete/<int:pk>/", CartDeleteView.as_view(), name="cart_delete"),
]