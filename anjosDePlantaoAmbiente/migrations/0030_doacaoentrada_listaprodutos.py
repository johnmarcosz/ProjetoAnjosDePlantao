# Generated by Django 2.0.13 on 2019-08-31 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anjosDePlantaoAmbiente', '0029_remove_doacaoentrada_listaprodutos'),
    ]

    operations = [
        migrations.AddField(
            model_name='doacaoentrada',
            name='listaProdutos',
            field=models.ManyToManyField(to='anjosDePlantaoAmbiente.ProdutoDoado'),
        ),
    ]
