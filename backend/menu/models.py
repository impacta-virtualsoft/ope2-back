from django.db import models

from backend.core.models import ModelBase
from backend.menu.constants import TYPE_PRODUCT_MENU, TYPE_REVENUE_MENU, WEEK_DAY
from backend.product.constants import TYPE_PRODUCT
from backend.product.models import Product, Revenue


class Menu(ModelBase):
    description = models.CharField(max_length=200)
    weekday = models.IntegerField(
        choices=WEEK_DAY, default=0, verbose_name="Dia da Semana"
    )
    status = models.IntegerField(choices=((0, "Inativo"), (1, "Ativo")), default=1)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "Cardápio"
        verbose_name = "Cardápio"


# class Items(ModelBase):
#     product = models.ForeignKey(
#         Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Produto"
#     )
#     revenue = models.ForeignKey(
#         Revenue, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Receita"
#     )
#     type = models.IntegerField(
#         choices=MENU_TYPE, default=0, verbose_name="Tipo do Produto"
#     )
#
#     def __str__(self):
#         if self.product is None:
#             return self.revenue.description
#         else:
#
#             return self.product.description
#
#     class Meta:
#         verbose_name_plural = "Itens para Cardápio"
#         verbose_name = "Item para Cardápio"
#
#
# class MenuItems(ModelBase):
#     items = models.ForeignKey(
#         Items, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Itens"
#     )
#     menu = models.ForeignKey(
#         Menu, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Cardápio"
#     )
#     value = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
#     status = models.IntegerField(choices=((0, 'Inativo'), (1, 'Ativo')), default=1)
#
#     def __str__(self):
#         return self.items.__str__()
#
#     class Meta:
#         verbose_name_plural = "Itens do Cardápio"
#         verbose_name = "Item do Cardápio"


# DRINK, LUNCH, DESSERT, PORTION, ADDITIONAL
class RevenueMenu(ModelBase):
    revenue = models.ForeignKey(
        Revenue, on_delete=models.CASCADE, verbose_name="Receitas"
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Cardápio"
    )
    type = models.IntegerField(
        choices=TYPE_REVENUE_MENU, default=0, verbose_name="Tipo de Receita"
    )
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    status = models.IntegerField(choices=((0, "Inativo"), (1, "Ativo")), default=1)

    def __str__(self):
        return self.revenue.__str__()

    class Meta:
        verbose_name_plural = "Cardapio de Receitas"
        verbose_name = "Cardapio de Receita"


class ProductMenu(ModelBase):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Produtos"
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Cardápio"
    )
    type = models.IntegerField(
        choices=TYPE_PRODUCT_MENU, default=0, verbose_name="Tipo de Produto"
    )
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    status = models.IntegerField(choices=((0, "Inativo"), (1, "Ativo")), default=1)

    def __str__(self):
        return self.product.__str__()

    class Meta:
        verbose_name_plural = "Cardapio de Produtos"
        verbose_name = "Cardapio de Produto"
