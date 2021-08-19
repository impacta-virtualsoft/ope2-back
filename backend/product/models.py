from django.db import models
from backend.core.models import ModelBase
from backend.product.constants import TYPE_PRODUCT, INGREDIENT

class Product(ModelBase):
    description = models.CharField(max_length=200)
    type = models.IntegerField(choices=TYPE_PRODUCT, default=0, verbose_name='Tipo de Produto')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Produtos'
        verbose_name = 'Produto'
        ordering = ['description', ]

class Revenue(ModelBase):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Receitas'
        verbose_name = 'Receita'
        ordering = ['description', ]

class RevenueProduct(ModelBase):
    revenue = models.ForeignKey(Revenue, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, limit_choices_to={'type': INGREDIENT})

    def __str__(self):
        return self.revenue.description

    class Meta:
        verbose_name_plural = 'Produtos da Receita'
        verbose_name = 'Produto da Receita'