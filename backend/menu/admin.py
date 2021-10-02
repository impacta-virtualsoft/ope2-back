from django.contrib.admin import ModelAdmin, StackedInline, register

from .models import Menu, RevenueMenu, ProductMenu, AdditionalMenu


class RevenueMenuInLineAdmin(StackedInline):
    model = RevenueMenu
    extra = 0
    suit_classes = "suit-tab suit-tab-produtos"


class ProductMenuInLineAdmin(StackedInline):
    model = ProductMenu
    extra = 0
    suit_classes = "suit-tab suit-tab-produtos"

class ProductMenuInLineAdmin(StackedInline):
    model = ProductMenu
    extra = 0
    suit_classes = "suit-tab suit-tab-produtos"


@register(Menu)
class Menu(ModelAdmin):
    inlines = [
        RevenueMenuInLineAdmin,
        ProductMenuInLineAdmin,
    ]
    list_display = ["weekday"]
