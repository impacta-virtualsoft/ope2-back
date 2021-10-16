from django.db import models

from backend.core.models import ModelBase
from backend.product.constants import INGREDIENT, TYPE_PRODUCT


class UnitMeasure(ModelBase):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=2)

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name_plural = "Unidades de Medida"
        verbose_name = "Unidade de Medida"


class Product(ModelBase):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    type = models.IntegerField(
        choices=TYPE_PRODUCT, default=0, verbose_name="Tipo de Produto"
    )
    unit_measure = models.ForeignKey(UnitMeasure, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Produtos"
        verbose_name = "Produto"
        ordering = [
            "description",
        ]


class Recipe(ModelBase):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "Receitas"
        verbose_name = "Receita"
        ordering = [
            "name",
        ]


class RecipeProduct(ModelBase):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="recipe_product"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        limit_choices_to={"type": INGREDIENT},
    )
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.recipe.name

    class Meta:
        verbose_name_plural = "Produtos da Receita"
        verbose_name = "Produto da Receita"
