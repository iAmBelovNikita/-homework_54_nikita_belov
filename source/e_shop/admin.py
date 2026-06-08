from django.contrib import admin

from .models import Category, Product

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


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)