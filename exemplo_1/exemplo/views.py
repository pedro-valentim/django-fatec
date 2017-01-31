from django.shortcuts import render
import datetime


def current_datetime(request):
    nome = ''
    if request.method == 'POST':
        nome = request.POST.get('nome')
    now = datetime.datetime.now()
    return render(request, 'home.html', {'nome': nome, 'now': now})
