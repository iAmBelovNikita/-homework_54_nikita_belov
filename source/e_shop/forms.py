from django import forms
from django.forms import TextInput, Textarea, NumberInput, TelInput
from django.forms.widgets import Select

from .models import Category, Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "description", "category", "price", "remains", "image_link"]
        widgets = {
            "title": TextInput(attrs={"class": "form-control"}),
            "description": Textarea(attrs={"class": "form-control", "rows": "5"}),
            "category": Select(attrs={"class": "form-control"}),
            "price": NumberInput(attrs={"class": "form-control"}),
            "remains": NumberInput(attrs={"class": "form-control"}),
            "image_link": TextInput(attrs={"class": "form-control"}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title", "description"]
        widgets = {
            "title": TextInput(attrs={"class": "form-control"}),
            "description": Textarea(attrs={"class": "form-control", "rows": "5"}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["name", "phone", "address"]
        widgets = {
            "name": TextInput(attrs={"class": "form-control", "placeholder": "Your name"}),
            "phone": TelInput(attrs={"class": "form-control", "placeholder": "+996 ..."}),
            "address": TextInput(attrs={"class": "form-control", "placeholder": "Delivery address"}),
        }