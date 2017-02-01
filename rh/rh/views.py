# coding: utf8
from django.shortcuts import render


def home(request, **kwargs):
    return render(request, 'home.html', {})
