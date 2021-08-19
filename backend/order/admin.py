from django.contrib.admin import ModelAdmin, register

from .models import SalesOrder


@register(SalesOrder)
class SalesOrderAdmin(ModelAdmin):
    ...
