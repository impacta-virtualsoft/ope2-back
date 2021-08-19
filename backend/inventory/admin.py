from django.contrib.admin import ModelAdmin, register

from .models import Inventory

@register(Inventory)
class InventoryAdmin(ModelAdmin):
    ...
