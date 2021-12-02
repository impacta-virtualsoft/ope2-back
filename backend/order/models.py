from django.db import models

from backend.core.models import Client, ModelBase
from backend.menu.models import RecipeMenu, ProductMenu
from backend.order.constants import STATUS_ORDER, TYPE_ORDER
from backend.product.models import Product


class StatusOrder(ModelBase):
    name = models.CharField(max_length=200, verbose_name='Nome')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Status dos Pedidos"
        verbose_name = "Status do Pedido"


class TypeOrder(ModelBase):
    name = models.CharField(max_length=200, verbose_name='Nome')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tipo de Pedido"
        verbose_name = "Tipos de Pedidos"


class SalesOrder(ModelBase):
    status_order = models.ForeignKey(StatusOrder, on_delete=models.CASCADE, default=1)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    comments = models.CharField(verbose_name="Observações", max_length=200, blank=True)
    type = models.ForeignKey(TypeOrder, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)

    def __str__(self):
        return f"{self.id} - {self.type.__str__()} - {self.client.name}"

    class Meta:
        verbose_name_plural = "Pedidos de Venda"
        verbose_name = "Pedido de Venda"


class SalesOrderRecipe(ModelBase):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name="recipe_order")
    recipe = models.ForeignKey(RecipeMenu, on_delete=models.CASCADE, verbose_name="Receitas")

    def __str__(self):
        return f"{self.sales_order.id} - {self.recipe.__str__()}"

    class Meta:
        verbose_name_plural = "ReceitasMenu Pedidos"
        verbose_name = "ReceitaMenu Pedido"


class SalesOrderProduct(ModelBase):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name="product_order")
    product = models.ForeignKey(ProductMenu, on_delete=models.CASCADE, verbose_name="Produtos")

    def __str__(self):
        return f"{self.sales_order.id} - {self.product.__str__()}"

    class Meta:
        verbose_name_plural = "ProdutoMenus Pedidos"
        verbose_name = "ProdutoMenu Pedido"
