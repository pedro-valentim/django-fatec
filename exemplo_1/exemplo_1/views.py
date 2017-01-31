import datetime
from django.shortcuts import render


def home(request):
    nome = ''
    if request.method == 'POST':
        nome = request.POST.get('nome')
    now = datetime.datetime.now()
    # html = "<html><body>Hello , %s! It is now %s.</body></html>" % (nome,now)
    return render(request, 'home.html', {'nome': nome, 'now': now})
