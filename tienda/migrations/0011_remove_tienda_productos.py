# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0010_remove_tienda_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tienda',
            name='productos',
        ),
    ]
