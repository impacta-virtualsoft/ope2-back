from django.contrib.admin import ModelAdmin, register

from .models import Client, Provider


@register(Client)
class ClientAdmin(ModelAdmin):
    ...


@register(Provider)
class ProviderAdmin(ModelAdmin):
    ...
