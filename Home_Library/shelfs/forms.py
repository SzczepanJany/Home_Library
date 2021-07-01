from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import widgets
import datetime

from django.forms.fields import DateField

from .models import  Genre, Item, Publisher, Rate, User, Serie


class LoginForm(forms.Form):
    username = forms.CharField(max_length=12)
    password = forms.CharField(max_length=16, widget=forms.PasswordInput)


class CreateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=12, label='Login')
    password = forms.CharField(max_length=16,label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=16,label='Powtórz hasło', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'birthday', 'description','file']
        labels = {'email':'email','birthday':'Data ur.' , 'description':'Opis','file':'Zdjęcie'}
        cur_year = datetime.datetime.today().year
        year_range = tuple([i for i in range(cur_year - 120, cur_year-6)])
        widgets = {'birthday':widgets.SelectDateWidget(years=year_range)}

    def clean(self) :
        clean_data =  super().clean()
        pas1 = clean_data['password']
        pas2 = clean_data['password2']
        if pas1 != pas2:
            raise ValidationError('Hasła się nie zgadzają')


class CreateNewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'isbn', 'genre', 'description','file', 'cathegory', 'year', 'serie', 'volume', 'notice', 'publisher', 'edition', 'language']
        labels = {'title':'Nazwa', 'genre':'Gatunek', 'description':'Opis','file':'Okładka', 'cathegory':'Categoria', 'year':'Rok', 'serie':'Seria', 'volume':'Część', 'notice':'Uwagi', 'publisher':'Wydawca', 'edition':'Edycja', 'language':'Język'}
        widgets = {"genre" : forms.Select()} 
        
    def clean(self):
        # validacja ISBN
        pass

class CreateNewGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'description']
        labels = {'name':'Nazwa', 'description':'Opis'}


class CreateNewSerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ['name', 'world', 'nr_of_volumes', 'description', 'file']
        labels = {'name':'Nazwa','world': 'Świat', 'nr_of_volumes':'Liczba woluminów', 'description':'Opis', 'file':'Dodaj zdjęcie'}


class CreateNewPublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'city', 'country', 'description', 'file']
        labels = {'name':'Nazwa','city': "Miasto", 'country':"Kraj", 'description':'Opis', 'file':'Dodaj zdjęcie'}


# class CreateNewRateForm(forms.ModelForm):
#     class Meta:
#         model = Rate
#         fields = ['name', 'city', 'country', 'description']
#         labels = {'name':'Nazwa','city': "Miasto", 'country':"Kraj", 'description':'Opis'}