from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=120, unique=True)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        db_table = "Category"

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_link = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Product"
        verbose_name = "Product"