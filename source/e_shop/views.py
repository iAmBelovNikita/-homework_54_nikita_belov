from django.shortcuts import render, get_object_or_404, redirect

from decimal import Decimal, InvalidOperation

from .models import Product, Category


# Create your views here.

def products_view(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product.html", {"product": product})

def product_add_view(request):
    categories = Category.objects.all()

    if request.method == "GET":
        return render(request, "product_add.html", {
            "categories": categories
        })

    elif request.method == "POST":
        title = request.POST.get("title", "").strip()
        price = request.POST.get("price", "").strip()
        image_link = request.POST.get("image_link", "").strip()
        category_id = request.POST.get("category")
        description = request.POST.get("description", "").strip()

        if not title or not price or not image_link or not category_id:
            return render(request, "product_add.html", {
                "categories": categories,
                "error": "Title, price, image url and category are required",
                "title": title,
                "price": price,
                "image_link": image_link,
                "description": description,
                "selected_category_id": category_id,
            })

        try:
            price = Decimal(price)
        except InvalidOperation:
            return render(request, "product_add.html", {
                "categories": categories,
                "error": "Price must be a number",
                "title": title,
                "price": request.POST.get("price", ""),
                "image_link": image_link,
                "description": description,
                "selected_category_id": category_id,
            })

        if price < 0:
            return render(request, "product_add.html", {
                "categories": categories,
                "error": "Price cannot be negative",
                "title": title,
                "price": price,
                "image_link": image_link,
                "description": description,
                "selected_category_id": category_id,
            })

        category = get_object_or_404(Category, pk=category_id)

        product = Product.objects.create(
            title=title,
            price=price,
            image_link=image_link,
            category=category,
            description=description,
        )

        return redirect("product_view", pk=product.pk)

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