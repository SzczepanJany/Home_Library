from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django_countries.fields import CountryField
from datetime import date
from django.conf import settings
from django.utils import timezone

from Home_Library.settings import LANGUAGE_CODE

CATHEGORY = (
    (1, 'Book'),
    (2, 'eBook'),
    (3, 'Audiobook'),
    (4, 'Moovie'),
    (5, 'PC Game'),
    (6, 'PS Game'),
    (7, 'N Game'),
    (8, 'Audio CD'),
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

LANGUAGE=(
    (1, 'Polish'),
    (2, 'English'),
    (3, 'German'),
    (4, 'French'),
    (5, 'Other')
)


class User(AbstractUser):
    birthday = models.DateField(null=True)
    death = models.DateField(null=True)
    plc_of_brth = models.CharField(max_length=30, null=True)
    plc_of_dth = models.CharField(max_length=30, null=True)
    nationality = CountryField()
    file = models.FileField(null=True)
    description = models.CharField(max_length=400,null=True)


class UserItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_items', on_delete=CASCADE)
    item = models.ForeignKey('Item', related_name='user_items', on_delete=CASCADE)
    is_author = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_editor = models.BooleanField(default=False)
    favourite = models.BooleanField(default=False)
    nr_of_copies = models.IntegerField(default=1)


class Serie(models.Model):
    name = models.CharField(max_length=128)
    world = models.CharField(max_length=128)
    nr_of_volumes = models.IntegerField(default=1)
    file = models.FileField(null=True)
    description = models.CharField(max_length=400,null=True)


class Publisher(models.Model):
    name = models.CharField(max_length=128, unique=True)
    city = models.CharField(max_length=128, null=True)
    country = CountryField()
    file = models.FileField(null=True)
    description = models.CharField(max_length=400,null=True)


class Rate(models.Model):
    item = models.OneToOneField('Item', related_name='rates', on_delete=CASCADE)
    user = models.OneToOneField(User, on_delete=CASCADE, related_name='rates')
    rate = models.IntegerField(choices=RATE)
    file = models.FileField(null=True)
    description = models.CharField(max_length=400,null=True)


class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    file = models.FileField(null=True)
    description = models.CharField(max_length=400,null=True)

    @property
    def sub_name(self):
        return "{}".format(self.name)

    def __str__(self):
        return self.sub_name


class Item(models.Model):
    title = models.CharField(max_length=128, unique=True)
    user = models.ManyToManyField(User, through=UserItem, related_name='items')
    isbn = models.CharField(max_length=13)
    genre = models.ManyToManyField(Genre)
    file = models.FileField(null=True)
    description = models.CharField(max_length=400,null=True)
    cathegory = models.IntegerField(choices=CATHEGORY)
    year = models.IntegerField(null=True)
    serie = models.ForeignKey(Serie, on_delete=CASCADE, null=True)
    volume = models.IntegerField(null=True)
    notice = models.CharField(max_length=80, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=CASCADE, null=True)
    edition = models.CharField(max_length=80, null=True)
    language = models.IntegerField(choices=LANGUAGE)


class Loan(models.Model):
    item = models.ForeignKey(Item, on_delete=CASCADE, related_name='loans')
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='loans')
    date_of_loan = models.DateField(default=timezone.now)
    date_of_return = models.DateField(null=True)
    in_loan = models.BooleanField(default=True)
    file = models.FileField(null=True)
    description = models.CharField(max_length=400,null=True)

