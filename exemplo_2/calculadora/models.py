# coding: utf8
from django.db import models


class LogSoma(models.Model):
    nome = models.CharField(u'Nome', help_text=u'Digite seu nome por favor', unique=True, max_length=100)
    num_1 = models.IntegerField(u'Número 1')
    num_2 = models.IntegerField(u'Número 2')

    datahora = models.DateTimeField(u'Data/Hora da Soma', auto_now_add=True)

    class Meta:
        verbose_name = u'Log de Soma'
