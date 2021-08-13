from django.db import models
from backend.core.models import ModelBase


class Product(ModelBase):
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Produtos'
        verbose_name = 'Produto'
        ordering = ['description', ]
