from django import forms
from django.forms import TextInput, Textarea, NumberInput
from django.forms.widgets import Select

from .models import Category


class ProductForm(forms.Form):
    title = forms.CharField(
        required=True,
        max_length=200,
        label="Title",
        widget=TextInput(attrs={"class": "form-control"})
    )

    description = forms.CharField(
        required=False,
        max_length=500,
        label="Description",
        widget=Textarea(attrs={"class": "form-control", "rows": "5"})
    )

    category = forms.ModelChoiceField(
        required=True,
        queryset=Category.objects.all(),
        label="Category",
        widget=Select(attrs={"class": "form-control"})
    )

    price = forms.DecimalField(
        required=True,
        max_digits=7,
        decimal_places=2,
        label="Price",
        widget=NumberInput(attrs={"class": "form-control"})
    )

    remains = forms.IntegerField(
        required=True,
        min_value=0,
        label="Remains",
        widget=NumberInput(attrs={"class": "form-control"})
    )

    image_link = forms.URLField(
        required=True,
        label="Image url",
        widget=TextInput(attrs={"class": "form-control"})
    )