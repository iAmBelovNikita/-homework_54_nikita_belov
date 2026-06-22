from django.views.generic import CreateView
from django.urls import reverse_lazy

from ..forms import CategoryForm
from ..models import Category

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "category/category_add.html"
    success_url = reverse_lazy("products_view")