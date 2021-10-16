from django.contrib.admin import ModelAdmin, StackedInline, register

from backend.product.models import Product, Recipe, RecipeProduct, UnitMeasure


@register(Product)
class ProductAdmin(ModelAdmin):
    ...


class RecipeProductInLineAdmin(StackedInline):
    model = RecipeProduct
    extra = 0
    suit_classes = "suit-tab suit-tab-produtos"


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    inlines = [
        RecipeProductInLineAdmin,
    ]
    list_display = ["description"]


@register(UnitMeasure)
class UnitMeasureAdmin(ModelAdmin):
    ...
