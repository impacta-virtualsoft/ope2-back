from django.db import models

from backend.core.models import ModelBase
from backend.menu.constants import TYPE_PRODUCT_MENU, TYPE_REVENUE_MENU, WEEK_DAY
from backend.product.constants import TYPE_PRODUCT
from backend.product.models import Product, Recipe


class Menu(ModelBase):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    monday = models.BooleanField(default=False, verbose_name="Segunda-Feira")
    tuesday = models.BooleanField(default=False, verbose_name="Terça-Feira")
    wednesday = models.BooleanField(default=False, verbose_name="Quarta-Feira")
    thursday = models.BooleanField(default=False, verbose_name="Quinta-Feira")
    friday = models.BooleanField(default=False, verbose_name="Sexta-Feira")
    saturday = models.BooleanField(default=False, verbose_name="Sábado")
    sunday = models.BooleanField(default=False, verbose_name="Domingo")
    status = models.IntegerField(choices=((0, "Inativo"), (1, "Ativo")), default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cardápio"
        verbose_name = "Cardápio"


# class Items(ModelBase):
#     product = models.ForeignKey(
#         Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Produto"
#     )
#     recipe = models.ForeignKey(
#         Recipe, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Receita"
#     )
#     type = models.IntegerField(
#         choices=MENU_TYPE, default=0, verbose_name="Tipo do Produto"
#     )
#
#     def __str__(self):
#         if self.product is None:
#             return self.recipe.description
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
class RecipeMenu(ModelBase):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, verbose_name="Receitas"
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Cardápio", related_name="recipe_menu"
    )
    type = models.IntegerField(
        choices=TYPE_REVENUE_MENU, default=1, verbose_name="Tipo de Receita"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    status = models.IntegerField(choices=((0, "Inativo"), (1, "Ativo")), default=1)

    def __str__(self):
        return self.recipe.__str__()

    class Meta:
        verbose_name_plural = "Cardapio de Receitas"
        verbose_name = "Cardapio de Receita"


class ProductMenu(ModelBase):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Produtos"
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Cardápio", related_name="product_menu"
    )
    type = models.IntegerField(
        choices=TYPE_PRODUCT_MENU, default=0, verbose_name="Tipo de Produto"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    status = models.IntegerField(choices=((0, "Inativo"), (1, "Ativo")), default=1)

    def __str__(self):
        return self.product.__str__()

    class Meta:
        verbose_name_plural = "Cardapio de Produtos"
        verbose_name = "Cardapio de Produto"
