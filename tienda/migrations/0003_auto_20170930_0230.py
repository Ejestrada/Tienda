# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_auto_20170930_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tienda',
            name='correo',
            field=models.EmailField(max_length=254),
        ),
    ]
