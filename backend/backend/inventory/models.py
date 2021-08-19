from django.db import models
from backend.core.models import ModelBase
from backend.product.models import Product

class Inventory(ModelBase):
    buy_date = models.DateField(verbose_name='Data da Compra')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Estoque de Mercadorias"
        verbose_name = "Estoque de Mercadoria"
