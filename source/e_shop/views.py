from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm
from .models import Product, Category


# Create your views here.

def products_view(request):
    products = Product.objects.filter(remains__gt=0).order_by(Lower("category__title"), Lower("title"))
    return render(request, "index.html", {"products": products})

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product.html", {"product": product})


def product_add_view(request):
    form = ProductForm()

    if request.method == 'GET':
        context = {'form': form}
        return render(request, 'product_add.html', context)

    elif request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            product = Product(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                category=form.cleaned_data.get('category'),
                price=form.cleaned_data.get('price'),
                remains=form.cleaned_data.get('remains'),
                image_link=form.cleaned_data.get('image_link'),
            )
            product.save()

            return redirect('product_view', pk=product.pk)

        context = {'form': form}
        return render(request, 'product_add.html', context)

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