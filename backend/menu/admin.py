from django.contrib.admin import ModelAdmin, register, StackedInline

from .models import Items, Menu, MenuItems


@register(Items)
class Items(ModelAdmin):
    ...


class MenuItemsInLineAdmin(StackedInline):
    model = MenuItems
    extra = 0
    suit_classes = 'suit-tab suit-tab-produtos'


@register(Menu)
class Menu(ModelAdmin):
    inlines = [MenuItemsInLineAdmin,]
    list_display = ['weekday']
