from django.db import models
from backend.core.models import ModelBase, Client
from backend.product.models import Product
from backend.order.constants import STATUS_ORDER, TYPE_ORDER


class SalesOrder(ModelBase):
    status_order = models.IntegerField(choices=STATUS_ORDER, default=0, verbose_name='Status')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comments = models.CharField(verbose_name="Observações", max_length=200, blank=True)
    type = models.IntegerField(choices=TYPE_ORDER, default=0, verbose_name='Tipo de Pedido')

    class Meta:
        verbose_name_plural = "Pedidos de Venda"
        verbose_name = "Pedido de Venda"
