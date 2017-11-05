# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=80)),
                ('direccion', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
