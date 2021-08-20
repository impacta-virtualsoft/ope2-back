from django.contrib.admin import ModelAdmin, register
from django.contrib.admin.models import LogEntry

from .models import Client, Provider


@register(Client)
class ClientAdmin(ModelAdmin):
    ...


@register(Provider)
class ProviderAdmin(ModelAdmin):
    ...


@register(LogEntry)
class LogAdmin(ModelAdmin):
    ...
