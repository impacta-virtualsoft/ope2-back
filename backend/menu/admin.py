from django.contrib.admin import ModelAdmin, StackedInline, register

from .models import Menu, ProductMenu, RecipeMenu, TypeRecipeMenu, TypeProductMenu


class RecipeMenuInLineAdmin(StackedInline):
    model = RecipeMenu
    extra = 0
    suit_classes = "suit-tab suit-tab-produtos"


class ProductMenuInLineAdmin(StackedInline):
    model = ProductMenu
    extra = 0
    suit_classes = "suit-tab suit-tab-produtos"


@register(Menu)
class MenuAdmin(ModelAdmin):
    inlines = [
        RecipeMenuInLineAdmin,
        ProductMenuInLineAdmin,
    ]


@register(TypeProductMenu)
class TypeProductMenuAdmin(ModelAdmin):
    ...


@register(TypeRecipeMenu)
class TypeRecipeMenuAdmin(ModelAdmin):
    ...
