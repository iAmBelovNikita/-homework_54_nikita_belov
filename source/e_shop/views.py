from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Category


# Create your views here.

def products_view(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product.html", {"product": product})

def category_add_view(request):
    if request.method == "GET":
        return render(request, "category_add.html")

    elif request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()

        if not title:
            return render(request, "category_add.html", {
                "error": "Title is required",
                "title": title,
                "description": description,
            })

        if Category.objects.filter(title=title).exists():
            return render(request, "category_add.html", {
                "error": "Category with this title already exists",
                "title": title,
                "description": description,
            })

        Category.objects.create(
            title=title,
            description=description
        )

        return redirect("products_view")