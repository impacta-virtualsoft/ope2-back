from django.db import models
from backend.core.models import ModelBase
from backend.product.constants import TYPE_PRODUCT

class Product(ModelBase):
    description = models.CharField(max_length=200)
    type = models.IntegerField(choices=TYPE_PRODUCT, default=0, verbose_name='Tipo de Produto')

    class Meta:
        verbose_name_plural = 'Produtos'
        verbose_name = 'Produto'
        ordering = ['description', ]

class Revenue(ModelBase):
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Receitas'
        verbose_name = 'Receita'
        ordering = ['description', ]

class RevenueProduct(ModelBase):
    revenue = models.ForeignKey(Revenue, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Produtos da Receita'
        verbose_name = 'Produto da Receita'
