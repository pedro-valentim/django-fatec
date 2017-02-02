# coding: utf8
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
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
