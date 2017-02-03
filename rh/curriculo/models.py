# coding: utf8
from django.db import models
from django.contrib.auth.models import User


class Aluno(models.Model):
    nome = models.CharField(u'Nome', max_length=100)
    email = models.EmailField(u'Email', max_length=255, null=True, blank=True)
    telefone = models.CharField(u'Telefone', max_length=20, null=True, blank=True)
    site_pessoal = models.URLField(u'Site Pessoal', max_length=255, null=True, blank=True)
    facebook_link = models.URLField(u'Facebook', max_length=255, null=True, blank=True)
    github_link = models.URLField(u'GitHub', max_length=255, null=True, blank=True)
    linkedin_link = models.URLField(u'LinkedIn', max_length=255, null=True, blank=True)
    datacadastro = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User)

    def get_nome(self):
        return self.nome

    def __unicode__(self):
        return self.get_nome()

    def __str__(self):
        return self.get_nome()


class Curriculo(models.Model):
    arquivo = models.FileField()
    datacadastro = models.DateTimeField(auto_now_add=True)
    aluno = models.ForeignKey(Aluno, null=True)

    def __unicode__(self):
        return u'Curriculo: %i' % self.id

    def __str__(self):
        return u'Curriculo: %i' % self.id
