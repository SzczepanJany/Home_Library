from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.aggregates import Max
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from languages.fields import LanguageField, RegionField
from datetime import date

class User(AbstractUser):
    pass


CATHEGORY = (
    (1, 'Book'),
    (2, 'eBook'),
    (3, 'Audiobook')
    (4, 'Moovie'),
    (5, 'PC Game'),
    (6, 'PS Game'),
    (7, 'N Game'),
    (8, 'Audio CD')
    (9, 'Other')
)

AUTHOR_ROLE = (
    (1, 'Author'),
    (2, 'Translator'),
    (3, 'Artist'),
    (4, 'Programmer'),
    (5, 'Director'),
    (6, 'Other'),
)

RATE = (
    (1, 'Poor'),
    (2, 'Avarage'),
    (3, 'Good'),
    (4, 'Very good'),
    (5, 'Outstanding'),
    (6, 'Briliant'),
)

class Description(models.Model):
    pass


class Serie(models.Model):
    name = models.CharField(max_length=128)
    world = models.CharField(max_length=128)
    nr_of_volumes = models.IntegerField(default=1)
    description = models.ForeignKey(Description, on_delete=CASCADE, null=True)


class Publisher(models.Model):
    name = models.CharField(128)
    city = models.CharField(128, null=True)
    country = LanguageField()
    description = models.ForeignKey(Description, on_delete=CASCADE, null=True)


class Rate(models.Model):
    item = models.OneToOneField('Item')
    user = models.ForeignKey(User, on_delete=CASCADE)
    rate = models.IntegerField(choices=RATE)
    description = models.ForeignKey(Description, on_delete=CASCADE, null=True)


#models.Model czy models.User
class Author(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE)
    item = models.ManyToManyField('Item')
    role = models.IntegerField(choices=AUTHOR_ROLE)
    birthday = models.DateField(null=True)
    death = models.DateField(null=True)
    plc_of_brth = models.CharField(30, null=True)
    plc_of_dth = models.CharField(30, null=True)
    nationality = LanguageField()
    description = models.ForeignKey(Description, on_delete=CASCADE, null=True)


class Owner(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    item = models.ManyToManyField('Item')
    nr_of_copies = models.IntegerField(default=1)


class Genre(models.Model):
    name = models.CharField(max_length=20)
    description = models.ForeignKey(Description, on_delete=CASCADE, null=True)


class Item(models.Model):
    title = models.CharField(max_length=128)
    author = models.ManyToManyField(Author)
    isbn = models.CharField(max_length=13)
    genre = models.ManyToManyField(Genre)
    owner = models.ManyToManyField(Owner)
    description = models.ForeignKey(Description, on_delete=CASCADE, null=True)
    cathegory = models.IntegerField(choices=CATHEGORY)
    year = models.IntegerField(null=True)
    serie = models.ForeignKey(Serie, on_delete=CASCADE, null=True)
    volume = models.IntegerField(max_length=3, null=True)
    notice = models.CharField(max_length=80, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=CASCADE, null=True)
    edition = models.CharField(max_length=80, null=True)
    language = LanguageField()
    fauvourite = models.ManyToManyField(User)
    author_of_entry = models.ForeignKey(User, on_delete=CASCADE)


class Loan(models.Model):
    item = models.ForeignKey(Item, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)
    date_of_loan = models.DateField(default=date.today())
    date_of_return = models.DateField(null=True)
    in_loan = models.BooleanField(default=True)

