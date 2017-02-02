# coding: utf8
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm, LoginForm
from django.contrib.auth import (
    authenticate,
    logout as django_logout,
    login as django_login
)


def home(request, **kwargs):
    return render(request, 'home.html', {})


def logout(request, **kwargs):
    django_logout(request)
    return redirect('home')


def login(request, **kwargs):
    context = {}
    form = LoginForm(request.POST or {})
    if request.method == 'POST':
        if form.is_valid():
            username_form = form.cleaned_data['username']
            password_form = form.cleaned_data['password']
            user = authenticate(username=username_form, password=password_form)
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return redirect('home')
            else:
                messages.error(request, 'Usuário e senha não conferem!')
    context['form'] = form
    return render(request, 'login.html', context)


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
