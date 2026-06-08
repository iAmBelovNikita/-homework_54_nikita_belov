from django.urls import path

from .views import products_view, product_view, category_add_view, product_add_view, product_update_view, \
    product_delete_view

urlpatterns = [
    path("", products_view, name="products_view"),
    path("products/", products_view, name="products_list"),
    path("products/add/", product_add_view, name="product_add_view"),
    path("products/<int:pk>/", product_view, name="product_view"),
    path("products/<int:pk>/update/", product_update_view, name="product_update_view"),
    path('products/<int:pk>/delete/', product_delete_view, name='product_delete_view'),
    path("categories/add/", category_add_view, name="category_add_view"),
]