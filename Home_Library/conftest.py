import pytest
from django.contrib.auth.models import Permission

from shelfs.models import Author, Serie, User


@pytest.fixture
def logged_in_client(client):
    p = Permission.objects.get(codename='view_serie')
    p2 = Permission.objects.get(codename='add_serie')
    p3 = Permission.objects.get(codename='view_author')
    p4 = Permission.objects.get(codename='add_author')
    us = User.objects.create_user(
        username="test",
        password="pass",
    )
    us.user_permissions.add(p)
    us.user_permissions.add(p2)
    us.user_permissions.add(p3)
    us.user_permissions.add(p4)
    client.login(username='test', password='pass')


@pytest.fixture
def author():
    return Author.objects.create(
    name = 'Imię',
    surname = 'Nazwisko',
    birthday = '1959-03-16',
    nationality = 'US',
    description = 'African fiction writer'
    )

@pytest.fixture
def author():
    names = ['John','Edith', 'Ursula']
    for name in names:
        Author.objects.create(name=name, description='test')

@pytest.fixture
def serie():
    return Serie.objects.create(
    name = 'Jurrasic Park',
    world = 'Jurrasic',
    nr_of_volumes = '19'
    )

@pytest.fixture
def series():
    names = ['Tytani','Herosi', 'Samobójcy']
    for name in names:
        Serie.objects.create(name=name, world='test')