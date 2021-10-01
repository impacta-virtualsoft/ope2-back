from django.db import models

from backend.core.models import ModelBase
from backend.menu.constants import WEEK_DAY, MENU_TYPE
from backend.product.models import Product, Revenue
from backend.product.constants import RESALE, INGREDIENT, TYPE_PRODUCT


class Menu(ModelBase):
    description = models.CharField(max_length=200)
    weekday = models.IntegerField(
        choices=WEEK_DAY, default=0, verbose_name="Dia da Semana"
    )
    status = models.IntegerField(choices=((0, 'Inativo'),(1, 'Ativo')),default=1)

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
class LunchMenu(ModelBase):
    revenue = models.ForeignKey(
        Revenue, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Receita"
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Cardápio"
    )
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    status = models.IntegerField(choices=((0, 'Inativo'), (1, 'Ativo')), default=1)

    def __str__(self):
        return self.revenue.__str__()

    class Meta:
        verbose_name_plural = "Lanches"
        verbose_name = "Lanche"


class DrinkMenu(ModelBase):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, limit_choices_to={"type": RESALE}, verbose_name="Adicionais"
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Cardápio"
    )
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    status = models.IntegerField(choices=((0, 'Inativo'), (1, 'Ativo')), default=1)

    def __str__(self):
        return self.product.__str__()

    class Meta:
        verbose_name_plural = "Bebidas"
        verbose_name = "Bebida"


class DessertMenu(ModelBase):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, limit_choices_to={"type": INGREDIENT}, verbose_name="Adicionais"
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Cardápio"
    )
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    status = models.IntegerField(choices=((0, 'Inativo'), (1, 'Ativo')), default=1)

    def __str__(self):
        return self.product.__str__()

    class Meta:
        verbose_name_plural = "Sobremesas"
        verbose_name = "Sobremesa"


class PortionMenu(ModelBase):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, limit_choices_to={"type": INGREDIENT}, verbose_name="Adicionais"
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Cardápio"
    )
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    status = models.IntegerField(choices=((0, 'Inativo'), (1, 'Ativo')), default=1)

    def __str__(self):
        return self.product.__str__()

    class Meta:
        verbose_name_plural = "Porções"
        verbose_name = "Porção"


class AdditionalMenu(ModelBase):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, limit_choices_to={"type": INGREDIENT}, verbose_name="Adicionais"
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Cardápio"
    )
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    status = models.IntegerField(choices=((0, 'Inativo'), (1, 'Ativo')), default=1)

    def __str__(self):
        return self.product.__str__()

    class Meta:
        verbose_name_plural = "Adicionais"
        verbose_name = "Adicional"
