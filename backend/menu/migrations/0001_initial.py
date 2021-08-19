# Generated by Django 3.1.13 on 2021-08-19 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified_in', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Produto')),
                ('revenue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.revenue', verbose_name='Receita')),
            ],
            options={
                'verbose_name': 'Item do Cardápio',
                'verbose_name_plural': 'Itens do Cardápio',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified_in', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('weekday', models.IntegerField(choices=[(0, 'Domingo'), (1, 'Segunda-Feira'), (2, 'Terça-Feira'), (3, 'Quarta-Feira'), (4, 'Quinta-Feira'), (5, 'Sexta-Feira'), (6, 'Sábado')], default=0, verbose_name='Dia da Semana')),
            ],
            options={
                'verbose_name': 'Cardápio',
                'verbose_name_plural': 'Cardápio',
            },
        ),
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified_in', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('items', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.items', verbose_name='Itens')),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menu', verbose_name='Cardápio')),
            ],
            options={
                'verbose_name': 'Item do Cardápio',
                'verbose_name_plural': 'Itens do Cardápio',
            },
        ),
    ]