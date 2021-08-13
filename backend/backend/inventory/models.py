from django.db import models
from backend.core.models import ModelBase


class Inventory(ModelBase):
    buy_date = models.DateField(verbose_name='Data da Compra')

    class Meta:
        verbose_name_plural = "Estoque de Mercadorias"
        verbose_name = "Estoque de Mercadoria"
