# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogSoma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('num_1', models.IntegerField(verbose_name='N\xfamero 1')),
                ('num_2', models.IntegerField(verbose_name='N\xfamero 2')),
                ('datahora', models.DateTimeField(auto_now_add=True, verbose_name='Data/Hora da Soma')),
            ],
        ),
    ]
