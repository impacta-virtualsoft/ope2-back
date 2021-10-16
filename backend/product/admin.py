from django.contrib.admin import ModelAdmin, StackedInline, register

from backend.product.models import Product, Revenue, RevenueProduct, UnitMeasure


@register(Product)
class ProductAdmin(ModelAdmin):
    ...


class RevenueProductInLineAdmin(StackedInline):
    model = RevenueProduct
    extra = 0
    suit_classes = "suit-tab suit-tab-produtos"


@register(Revenue)
class RevenueAdmin(ModelAdmin):
    inlines = [
        RevenueProductInLineAdmin,
    ]
    list_display = ["description"]


@register(UnitMeasure)
class UnitMeasureAdmin(ModelAdmin):
    ...
