from django.contrib.admin import ModelAdmin, register, StackedInline

from backend.product.models import Product, Revenue, RevenueProduct


@register(Product)
class ProductAdmin(ModelAdmin):
    ...


class RevenueProductInLineAdmin(StackedInline):
    model = RevenueProduct
    extra = 0
    suit_classes = 'suit-tab suit-tab-produtos'


@register(Revenue)
class RevenueAdmin(ModelAdmin):
    inlines = [RevenueProductInLineAdmin,]
    list_display = ['description']

