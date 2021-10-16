from django.contrib.admin import ModelAdmin, StackedInline, register

from .models import Menu, ProductMenu, RecipeMenu


class RecipeMenuInLineAdmin(StackedInline):
    model = RecipeMenu
    extra = 0
    suit_classes = "suit-tab suit-tab-produtos"


class ProductMenuInLineAdmin(StackedInline):
    model = ProductMenu
    extra = 0
    suit_classes = "suit-tab suit-tab-produtos"


@register(Menu)
class Menu(ModelAdmin):
    inlines = [
        RecipeMenuInLineAdmin,
        ProductMenuInLineAdmin,
    ]
