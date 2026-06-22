from django.contrib import admin

from .models import Category, Product, OrderItem, Order


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ('title',)
    fields = ('title', 'description')
    search_fields = ('title', 'description')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price', 'remains', 'created_at', 'image_link')
    list_filter = ('category', 'created_at', 'price', 'remains')
    fields = ('title', 'description', 'category', 'price', 'remains', 'image_link', 'created_at')
    search_fields = ('title', 'description', 'category__title', 'price')
    readonly_fields = ('created_at',)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    inlines = [OrderItemInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)