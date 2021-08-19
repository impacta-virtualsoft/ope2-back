from django.db import models
from django.urls import reverse


class ModelBase(models.Model):
    created_in = models.DateTimeField(verbose_name="Criado em", auto_now_add=True)
    modified_in = models.DateTimeField(verbose_name="Modificado em", auto_now=True)

    class Meta:
        abstract = True


class Client(ModelBase):
    cpf = models.CharField(verbose_name="CPF", unique=True, max_length=11)
    name = models.CharField(verbose_name="Nome", max_length=200, blank=True)

    class Meta:
        verbose_name_plural = "Clientes"
        verbose_name = "Cliente"

    def __str__(self):
        return self.name


class Provider(ModelBase):
    cnpj = models.CharField(verbose_name="CNPJ", unique=True, max_length=14, blank=True, null=True)
    cpf = models.CharField(verbose_name="CPF", unique=True, max_length=11, blank=True, null=True)
    corporate_name = models.CharField(verbose_name="Razão Social", max_length=200, blank=True)

    class Meta:
        verbose_name_plural = "Fornecedores"
        verbose_name = "Fornecedor"

    def __str__(self):
        return self.name
