# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0005_aluno_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='email',
            field=models.EmailField(max_length=255, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='facebook_link',
            field=models.URLField(max_length=255, null=True, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='github_link',
            field=models.URLField(max_length=255, null=True, verbose_name='GitHub'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='linkedin_link',
            field=models.URLField(max_length=255, null=True, verbose_name='LinkedIn'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='site_pessoal',
            field=models.URLField(max_length=255, null=True, verbose_name='Site Pessoal'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='telefone',
            field=models.CharField(max_length=20, null=True, verbose_name='Telefone'),
        ),
    ]
