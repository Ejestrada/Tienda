# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0008_producto_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='tienda',
            name='Descripcion',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
