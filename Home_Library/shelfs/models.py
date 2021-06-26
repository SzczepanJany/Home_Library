from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from languages.fields import LanguageField, RegionField


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

class Description(models.Model):
    pass


class Serie(models.Model):
    pass


class Publisher(models.Model):
    pass


class Author(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE)
    item = models.ForeignKey('Item', on_delete=CASCADE)
    role = models.IntegerField(choices=AUTHOR_ROLE)


class Item(models.Model):
    title = models.CharField(max_length=128)
    author = models.ManyToManyField(User, through=Author)
    isbn = models.CharField(max_length=13)
    description = models.ForeignKey(Description, on_delete=CASCADE, null=True)
    cathegory = models.IntegerField(choices=CATHEGORY)
    year = models.IntegerField(null=True)
    serie = models.ForeignKey(Serie, on_delete=CASCADE, null=True)
    volume = models.IntegerField(max_length=3, null=True)
    notice = models.CharField(max_length=80, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=CASCADE, null=True)
    edition = models.CharField(max_length=80, null=True)
    language = LanguageField()
