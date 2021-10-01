from django.contrib.admin import ModelAdmin, StackedInline, register

from .models import Menu, LunchMenu, DrinkMenu, DessertMenu, PortionMenu, AdditionalMenu


class LunchMenuInLineAdmin(StackedInline):
    model = LunchMenu
    extra = 0
    suit_classes = "suit-tab suit-tab-produtos"


class DrinkMenuInLineAdmin(StackedInline):
    model = DrinkMenu
    extra = 0
    suit_classes = "suit-tab suit-tab-produtos"


class DessertMenuInLineAdmin(StackedInline):
    model = DessertMenu
    extra = 0
    suit_classes = "suit-tab suit-tab-produtos"


class PortionMenuInLineAdmin(StackedInline):
    model = PortionMenu
    extra = 0
    suit_classes = "suit-tab suit-tab-produtos"


class AdditionalMenuInLineAdmin(StackedInline):
    model = AdditionalMenu
    extra = 0
    suit_classes = "suit-tab suit-tab-produtos"


@register(Menu)
class Menu(ModelAdmin):
    inlines = [
        LunchMenuInLineAdmin,
        DrinkMenuInLineAdmin,
        DessertMenuInLineAdmin,
        PortionMenuInLineAdmin,
        AdditionalMenuInLineAdmin,
    ]
    list_display = ["weekday"]
