from django.contrib.admin import ModelAdmin, register

from backend.product.models import Product


@register(Product)
class ProductAdmin(ModelAdmin):
    ...
