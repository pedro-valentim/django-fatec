# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arquivo', models.FileField(upload_to=b'media/')),
                ('datacadastro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='aluno',
            name='datacadastro',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 1, 10, 51, 39, 242760), auto_now_add=True),
            preserve_default=False,
        ),
    ]
