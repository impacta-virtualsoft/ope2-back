# Generated by Django 3.1.13 on 2021-10-27 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified_in', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('monday', models.BooleanField(default=False, verbose_name='Segunda-Feira')),
                ('tuesday', models.BooleanField(default=False, verbose_name='Terça-Feira')),
                ('wednesday', models.BooleanField(default=False, verbose_name='Quarta-Feira')),
                ('thursday', models.BooleanField(default=False, verbose_name='Quinta-Feira')),
                ('friday', models.BooleanField(default=False, verbose_name='Sexta-Feira')),
                ('saturday', models.BooleanField(default=False, verbose_name='Sábado')),
                ('sunday', models.BooleanField(default=False, verbose_name='Domingo')),
                ('status', models.IntegerField(choices=[(0, 'Inativo'), (1, 'Ativo')], default=1)),
            ],
            options={
                'verbose_name': 'Cardápio',
                'verbose_name_plural': 'Cardápio',
            },
        ),
        migrations.CreateModel(
            name='TypeProductMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified_in', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Tipo de Produto',
                'verbose_name_plural': 'Tipos de Produto',
            },
        ),
        migrations.CreateModel(
            name='TypeRecipeMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified_in', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Tipo de Receita',
                'verbose_name_plural': 'Tipos de Receita',
            },
        ),
        migrations.CreateModel(
            name='RecipeMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified_in', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Inativo'), (1, 'Ativo')], default=1)),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_menu', to='menu.menu', verbose_name='Cardápio')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.recipe', verbose_name='Receitas')),
                ('type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='menu.typerecipemenu', verbose_name='Tipo de Receita')),
            ],
            options={
                'verbose_name': 'Cardapio de Receita',
                'verbose_name_plural': 'Cardapio de Receitas',
            },
        ),
        migrations.CreateModel(
            name='ProductMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified_in', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Inativo'), (1, 'Ativo')], default=1)),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_menu', to='menu.menu', verbose_name='Cardápio')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Produtos')),
                ('type', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='menu.typeproductmenu', verbose_name='Tipo de Produto')),
            ],
            options={
                'verbose_name': 'Cardapio de Produto',
                'verbose_name_plural': 'Cardapio de Produtos',
            },
        ),
    ]
