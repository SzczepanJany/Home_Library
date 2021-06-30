from django import forms
from django.core.exceptions import ValidationError

from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=12)
    password = forms.CharField(max_length=16, widget=forms.PasswordInput)


class CreateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=12)
    password = forms.CharField(max_length=16, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        
    def clean(self) :
        clean_data =  super().clean()
        pas1 = clean_data['password']
        pas2 = clean_data['password2']
        if pas1 != pas2:
            raise ValidationError('Hasła się nie zgadzają')