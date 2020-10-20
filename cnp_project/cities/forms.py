from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    """
    Form for collecting and validating data for creating a new User
    in the system.
    """

    username = forms.CharField(max_length=150, label='Логин')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Пользователь с таким логином уже существует')

        elif User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Пользователь с таким email уже существует')

        return cleaned_data

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        return user


class LoginForm(forms.Form):
    """
    Form for collecting and validating data for User authorization
    in the system.
    """

    username = forms.CharField(max_length=150, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
