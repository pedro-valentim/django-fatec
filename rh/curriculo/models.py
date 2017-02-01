# coding: utf8
from django.db import models


class Aluno(models.Model):
    nome = models.CharField(u'Nome', max_length=100)
    datacadastro = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.nome


class Curriculo(models.Model):
    arquivo = models.FileField()
    datacadastro = models.DateTimeField(auto_now_add=True)
    aluno = models.ForeignKey(Aluno, null=True)

    def __unicode__(self):
        return u'Currículo: %i' % self.id
