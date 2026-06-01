from django.shortcuts import render, get_object_or_404

from .models import Product


# Create your views here.

def products_view(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product.html", {"product": product})