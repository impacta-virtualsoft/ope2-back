from django.contrib.admin import ModelAdmin, StackedInline, register

from .models import SalesOrder, StatusOrder, TypeOrder, SalesOrderProduct, SalesOrderRecipe


@register(StatusOrder)
class StatusOrderAdmin(ModelAdmin):
    ...


@register(TypeOrder)
class TypeOrderAdmin(ModelAdmin):
    ...


class SalesOrderProductInLineAdmin(StackedInline):
    model = SalesOrderProduct
    extra = 0
    suit_classes = "suit-tab suit-tab-produtos"


class SalesOrderRecipeInLineAdmin(StackedInline):
    model = SalesOrderRecipe
    extra = 0
    suit_classes = "suit-tab suit-tab-produtos"


@register(SalesOrder)
class SalesOrderAdmin(ModelAdmin):
    inlines = [
        SalesOrderProductInLineAdmin,
        SalesOrderRecipeInLineAdmin,
    ]
    list_display = ["id"]
