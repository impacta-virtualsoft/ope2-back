from django.db import models
from backend.core.models import ModelBase
from backend.product.models import Product, Revenue
from backend.menu.constants import WEEK_DAY

class Items(ModelBase):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Produto')
    revenue = models.ForeignKey(Revenue, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Receita')

    def __str__(self):
        if self.product == None:
            return self.revenue.description
        else:

            return self.product.description

    class Meta:
        verbose_name_plural = "Itens do Cardápio"
        verbose_name = "Item do Cardápio"


class Menu(ModelBase):
    weekday = models.IntegerField(choices=WEEK_DAY, default=0, verbose_name='Dia da Semana')

    class Meta:
        verbose_name_plural = "Cardápio"
        verbose_name = "Cardápio"

class MenuItems(ModelBase):
    items = models.ForeignKey(Items, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Itens')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Cardápio')
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)

    def __str__(self):
        return self.items.__str__()
    class Meta:
        verbose_name_plural = "Itens do Cardápio"
        verbose_name = "Item do Cardápio"
