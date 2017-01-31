# coding: utf8
from django import forms
from .models import LogSoma


class SomaForm(forms.ModelForm):

    def clean_nome(self):
        data = self.cleaned_data['nome']
        if data == 'teste':
            raise forms.ValidationError('Não é permitido que seu nome seja teste.')

        return data

    def soma(self):
        num_1 = self.cleaned_data['num_1']
        num_2 = self.cleaned_data['num_2']
        return num_1 + num_2

    class Meta:
        model = LogSoma
        fields = ['nome', 'num_1', 'num_2', ]
