from django.contrib.admin import ModelAdmin, register

from .models import Menu, MenuItems


@register(Menu)
class MenuAdmin(ModelAdmin):
    ...

@register(MenuItems)
class MenuItemsAdmin(ModelAdmin):
    ...
