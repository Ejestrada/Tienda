# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_auto_20170930_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('existencia', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=60)),
                ('precio', models.DecimalField(max_digits=8, decimal_places=2)),
            ],
        ),
        migrations.AddField(
            model_name='bodega',
            name='producto',
            field=models.ForeignKey(to='tienda.Producto'),
        ),
        migrations.AddField(
            model_name='bodega',
            name='tienda',
            field=models.ForeignKey(to='tienda.Tienda'),
        ),
        migrations.AddField(
            model_name='tienda',
            name='productos',
            field=models.ManyToManyField(to='tienda.Producto', through='tienda.Bodega'),
        ),
    ]
