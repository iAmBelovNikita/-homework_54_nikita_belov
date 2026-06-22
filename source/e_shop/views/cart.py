from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.urls import reverse
from django.views.generic import ListView

from ..forms import OrderForm
from ..models import CartItem, Product, OrderItem


class CartView(ListView):
    model = CartItem
    template_name = "cart/cart.html"
    context_object_name = "cart_items"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = context["cart_items"]
        context["total"] = sum(item.total_price() for item in cart_items)
        context["order_form"] = OrderForm()
        context["order_url"] = reverse("order_create")
        return context


class CartAddView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if product.remains == 0:
            return redirect(request.META.get("HTTP_REFERER", "products_view"))

        cart_item, created = CartItem.objects.get_or_create(product=product)

        if not created:
            if cart_item.quantity < product.remains:
                cart_item.quantity += 1
                cart_item.save()

        return redirect(request.META.get("HTTP_REFERER", "products_view"))


class CartDeleteView(View):
    def post(self, request, pk):
        cart_item = get_object_or_404(CartItem, pk=pk)
        cart_item.delete()
        return redirect("cart_view")


class CartReduceView(View):
    def post(self, request, *args, **kwargs):
        cart_item = get_object_or_404(CartItem, pk=kwargs["pk"])

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

        return redirect("cart_view")

class OrderCreateView(View):
    def post(self, request, *args, **kwargs):
        cart_items = CartItem.objects.all()

        if not cart_items.exists():
            return redirect("cart_view")

        form = OrderForm(request.POST)
        if not form.is_valid():
            total = sum(item.total_price() for item in cart_items)
            return render(request, "cart/cart.html", {
                "cart_items": cart_items,
                "total": total,
                "order_form": form,
            })

        order = form.save()

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
            )

            item.product.remains -= item.quantity
            item.product.save()

        cart_items.delete()

        return redirect("products_view")