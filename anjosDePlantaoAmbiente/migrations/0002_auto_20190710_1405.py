# Generated by Django 2.0.13 on 2019-07-10 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anjosDePlantaoAmbiente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='autor',
        ),
        migrations.RenameField(
            model_name='pessoa',
            old_name='telefone1',
            new_name='telefone',
        ),
        migrations.RemoveField(
            model_name='caixageral',
            name='pessoa',
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='consulta',
            name='pessoa',
        ),
        migrations.RemoveField(
            model_name='doacao',
            name='pessoa',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='telefone2',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='tipoCadastroPessoaFisica',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='tipoCadastroPessoaJuridica',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='tipoPessoaDoador',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='tipoPessoaRecebedor',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='bairro',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='dataDeCadastro',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='observacoes',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='Evento',
        ),
    ]
