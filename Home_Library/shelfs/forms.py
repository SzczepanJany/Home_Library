from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields

from .models import  Genre, Item, User


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


class CreateNewItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'isbn', 'genre', 'description', 'cathegory', 'year', 'serie', 'volume', 'notice', 'publisher', 'edition', 'language']
        labels = {'title':'Nazwa', 'genre':'Gatunek', 'description':'Opis', 'cathegory':'Categoria', 'year':'Rok', 'serie':'Seria', 'volume':'Część', 'notice':'Uwagi', 'publisher':'Wydawca', 'edition':'Edycja', 'language':'Język'}
        widgets = {"genre" : forms.Select()} 
        
    def clean(self):
        # validacja ISBN
        pass

class CreateNewGenre(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'description']
        labels = {'name':'Nazwa', 'description':'Opis'}