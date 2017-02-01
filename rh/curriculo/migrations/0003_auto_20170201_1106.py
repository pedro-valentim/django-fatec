# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0002_auto_20170201_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculo',
            name='arquivo',
            field=models.FileField(upload_to=b''),
        ),
    ]
