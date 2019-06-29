from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class SignUpForm(UserCreationForm):
    username=forms.CharField(
        label=_("username"),
        max_length=100,
        widget = forms.TextInput(attrs={'class':'form-control'})
        )

    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
    )

class LogInForm(AuthenticationForm):
    username=forms.CharField(
        max_length=100,
        widget = forms.TextInput(attrs={'class':'form-control'})
        )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
    )
    