from django.db import models

from backend.core.models import ModelBase


class TypeProduct(ModelBase):
    name = models.CharField(max_length=200, verbose_name='Nome')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tipo de Produto"
        verbose_name = "Tipos de Produto"


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
    description = models.CharField(max_length=500, null=True, blank=True)
    type = models.ForeignKey(TypeProduct, default=0, on_delete=models.CASCADE, verbose_name="Tipo de Produto")
    unit_measure = models.ForeignKey(UnitMeasure, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.unit_measure.__str__()}'

    class Meta:
        verbose_name_plural = "Produtos"
        verbose_name = "Produto"
        ordering = [
            "description",
        ]


class Recipe(ModelBase):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

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
        limit_choices_to={"id": 1},
    )
    quantity = models.DecimalField(max_digits=12, decimal_places=4, default=0)

    def __str__(self):
        return self.recipe.name

    class Meta:
        verbose_name_plural = "Produtos da Receita"
        verbose_name = "Produto da Receita"
