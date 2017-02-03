# coding: utf8
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from curriculo.models import Aluno, Curriculo


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(widget=PasswordInput)


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        exclude = ('user', )


class CurriculoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop('request_user')
        super(CurriculoForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        instance = super(CurriculoForm, self).save(*args, **kwargs)
        instance.aluno = self.request_user.aluno
        instance.save()
        return instance

    class Meta:
        model = Curriculo
        exclude = ('aluno', )


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
