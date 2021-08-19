from django.db import models
from backend.core.models import ModelBase
from backend.product.models import Product, Revenue
from backend.menu.constants import WEEK_DAY

class MenuItems(ModelBase):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    revenue = models.ForeignKey(Revenue, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Itens do Cardápio"
        verbose_name = "Item do Cardápio"


class Menu(ModelBase):
    menu_items = models.ForeignKey(Product, on_delete=models.CASCADE)
    weekday = models.IntegerField(choices=WEEK_DAY, default=0, verbose_name='Dia da Semana')

    class Meta:
        verbose_name_plural = "Cardápio"
        verbose_name = "Cardápio"
