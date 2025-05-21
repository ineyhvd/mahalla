from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    is_admin = forms.BooleanField(required=False, label='Admin hisobi')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'is_admin')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Foydalanuvchi nomi')
    password = forms.CharField(label='Parol', widget=forms.PasswordInput)