# Generated by Django 4.2.5 on 2023-09-23 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=50)),
                ('departamento', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=50)),
                ('preco_custo', models.FloatField()),
                ('preco_venda', models.FloatField()),
                ('fornecedor', models.CharField(max_length=20)),
                ('categoria', models.CharField(max_length=20)),
            ],
        ),
    ]