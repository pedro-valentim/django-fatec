# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0003_auto_20170201_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculo',
            name='aluno',
            field=models.ForeignKey(to='curriculo.Aluno', null=True),
        ),
    ]
