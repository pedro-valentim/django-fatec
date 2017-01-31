from django.shortcuts import render
from .forms import SomaForm
# Create your views here.


def home(request, **kwargs):
    context = {}

    form = SomaForm(request.POST or {'num_1': 0, 'num_2': 0})

    context['form'] = form

    if form.is_valid():
        context['soma'] = form.soma()
        form.save()

    return render(request, 'home.html', context)
