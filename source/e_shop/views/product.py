from django.db.models import Q
from django.db.models.functions import Lower
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ..forms import ProductForm
from ..models import Product


class ProductListView(ListView):
    model = Product
    template_name = "product/index.html"
    context_object_name = "products"
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset().filter(remains__gt=0).order_by(Lower("category__title"), Lower("title"))
        query = self.request.GET.get("q", "").strip()
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "")
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product/product_add.html"

    def get_success_url(self):
        return reverse("product_view", kwargs={"pk": self.object.pk})

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product/product_update.html"

    def get_success_url(self):
        return reverse("product_view", kwargs={"pk": self.object.pk})

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("products_view")