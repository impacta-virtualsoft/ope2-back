from django.db import models
from django.urls import reverse


class ModelBase(models.Model):
    created_in = models.DateTimeField(verbose_name="Criado em", auto_now_add=True)
    modified_in = models.DateTimeField(verbose_name="Modificado em", auto_now=True)

    class Meta:
        abstract = True


class Address(ModelBase):
    cep = models.CharField(max_length=8, blank=True, null=True,verbose_name='CEP')
    logradouro = models.CharField(max_length=200, blank=True,null=True, verbose_name='Logradouro')
    complemento = models.CharField(max_length=100, blank=True, null=True, verbose_name='Complemento')
    bairro = models.CharField(max_length=200, blank=True, null=True, verbose_name='Bairro')
    localidade = models.CharField(max_length=200, blank=True, null=True, verbose_name='Localidade')
    uf = models.CharField(max_length=2, blank=True, null=True, verbose_name='UF')

    class Meta:
        verbose_name_plural = "Endereços"
        verbose_name = "Endereço"

    def __str__(self):
        return self.logradouro


class Client(ModelBase):
    cpf = models.CharField(
        verbose_name="CPF", max_length=11, blank=True, null=True
    )
    name = models.CharField(verbose_name="Nome", max_length=200, blank=True)
    address = models.ForeignKey(Address, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Endereço", related_name="address")

    class Meta:
        verbose_name_plural = "Clientes"
        verbose_name = "Cliente"

    def __str__(self):
        return self.name


class Provider(ModelBase):
    cnpj = models.CharField(
        verbose_name="CNPJ", unique=True, max_length=14, blank=True, null=True
    )
    cpf = models.CharField(
        verbose_name="CPF", unique=True, max_length=11, blank=True, null=True
    )
    corporate_name = models.CharField(
        verbose_name="Razão Social", max_length=200, blank=True
    )

    class Meta:
        verbose_name_plural = "Fornecedores"
        verbose_name = "Fornecedor"

    def __str__(self):
        return self.corporate_name
