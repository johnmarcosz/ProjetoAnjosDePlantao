# Generated by Django 2.0.13 on 2019-07-31 02:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anjosDePlantaoAmbiente', '0011_auto_20190712_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdutoDoacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataCadastro', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('descricao', models.CharField(max_length=50)),
                ('quantiaDoacao', models.DecimalField(blank=True, decimal_places=2, max_digits=20)),
                ('saldoEstoque', models.DecimalField(blank=True, decimal_places=2, max_digits=20)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='doacaoentrada',
            name='outrasDoacoes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='doacaosaida',
            name='outrasDoacoes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='doacaoentrada',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=11),
        ),
        migrations.AddField(
            model_name='doacaoentrada',
            name='produtoDoacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='anjosDePlantaoAmbiente.ProdutoDoacao'),
        ),
        migrations.AddField(
            model_name='doacaosaida',
            name='produtoDoacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='anjosDePlantaoAmbiente.ProdutoDoacao'),
        ),
    ]