# Generated by Django 2.0.13 on 2019-08-12 23:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0002_auto_20190711_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
