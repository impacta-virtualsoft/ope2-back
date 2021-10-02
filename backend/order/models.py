from django.db import models

from backend.core.models import Client, ModelBase
from backend.order.constants import STATUS_ORDER, TYPE_ORDER
from backend.product.models import Product


class SalesOrder(ModelBase):
    status_order = models.IntegerField(
        choices=STATUS_ORDER, default=0, verbose_name="Status"
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comments = models.CharField(verbose_name="Observações", max_length=200, blank=True)
    type = models.IntegerField(
        choices=TYPE_ORDER, default=0, verbose_name="Tipo de Pedido"
    )

    def __str__(self):
        return f"{self.id} - {self.get_type_display()} - {self.client.name}"

    class Meta:
        verbose_name_plural = "Pedidos de Venda"
        verbose_name = "Pedido de Venda"

# class AdditionalOrder(ModelBase):
#     product_menu = models.ForeignKey(
#         ProductMenu, on_delete=models.CASCADE, limit_choices_to={"type": TYPE_PRODUCT_MENU.ADDITIONAL}, verbose_name="Adicional"
#     )
#     revenue_menu = models.ForeignKey(
#         RevenueMenu, on_delete=models.CASCADE, limit_choices_to={"type": TYPE_REVENUE_MENU.LUNCH}, verbose_name="Lanches"
#     )
#
#     def __str__(self):
#         return self.product.__str__()
#
#     class Meta:
#         verbose_name_plural = "Adicionais no Pedido"
#         verbose_name = "Adicional no Pedido"
