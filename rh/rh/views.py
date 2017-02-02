# coding: utf8
from django.shortcuts import render
from django.contrib import messages
from .forms import UserForm


def home(request, **kwargs):
    return render(request, 'home.html', {})


def cadastro(request, **kwargs):
    context = {}
    form = UserForm(request.POST or {})
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastrado com sucesso.')
        else:
            messages.error(request, 'Não foi possível realizar o cadastro.')
    context['form'] = form
    return render(request, 'cadastro.html', context)
