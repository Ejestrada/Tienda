# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_auto_20170930_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tienda',
            old_name='title',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='tienda',
            name='author',
        ),
        migrations.RemoveField(
            model_name='tienda',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='tienda',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='tienda',
            name='text',
        ),
        migrations.AddField(
            model_name='tienda',
            name='correo',
            field=models.EmailField(blank=True, max_length=70),
        ),
        migrations.AddField(
            model_name='tienda',
            name='direccion',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='tienda',
            name='telefono',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
