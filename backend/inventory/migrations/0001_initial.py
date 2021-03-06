# Generated by Django 3.1.13 on 2021-12-05 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified_in', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('buy_date', models.DateField(verbose_name='Data da Compra')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': 'Estoque de Mercadoria',
                'verbose_name_plural': 'Estoque de Mercadorias',
            },
        ),
    ]
