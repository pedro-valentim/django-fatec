# coding: utf8
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from curriculo.models import Aluno


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(widget=PasswordInput)


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = PasswordInput()

    def save(self, *args, **kwargs):
        user = super(UserForm, self).save(*args, **kwargs)
        user.set_password(self.cleaned_data['password'])
        user.save()

        aluno = Aluno()
        aluno.user = user
        aluno.nome = user.first_name

        aluno.save()

        return user

    class Meta:
        model = User
        exclude = (
            'last_login',
            'is_superuser',
            'user_permissions',
            'groups',
            'is_staff',
            'is_active',
            'date_joined',
        )
