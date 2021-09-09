# Generated by Django 3.2.6 on 2021-09-09 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import productos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripción')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Precio')),
                ('categoria', models.CharField(choices=[('Abarrotes', 'Abarrotes'), ('Farmacia', 'Farmacia'), ('Electronica', 'Electrónica')], max_length=50, verbose_name='Categoria')),
                ('cantidad', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='cantidad')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to=productos.models.custom_upload_to, verbose_name='imagen')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('IdUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
                'ordering': ['creado'],
            },
        ),
    ]