# coding: utf8
from django.shortcuts import render


def home(request, **kwargs):
    return render(request, 'home.html', {})


def cadastro(request, **kwargs):
    context = {}
    # context['form'] = AlunoForm()
    return render(request, 'cadastro.html', context)
