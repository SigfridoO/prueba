# Generated by Django 3.2.6 on 2021-09-11 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=200, verbose_name='Nombre del producto'),
        ),
    ]
