import pytest
from django.contrib.auth.models import Permission
from datetime import datetime

from shelfs.models import Author, Genre, Publisher, Serie, User, Item, Rate


@pytest.fixture
def logged_in_client(client):
    p = Permission.objects.get(codename='view_serie')
    p2 = Permission.objects.get(codename='add_serie')
    p3 = Permission.objects.get(codename='view_author')
    p4 = Permission.objects.get(codename='add_author')
    p5 = Permission.objects.get(codename='view_genre')
    p6 = Permission.objects.get(codename='add_genre')
    p7= Permission.objects.get(codename='view_publisher')
    p8 = Permission.objects.get(codename='add_publisher')
    p9= Permission.objects.get(codename='view_rate')
    p10 = Permission.objects.get(codename='add_rate')
    p11= Permission.objects.get(codename='view_item')
    p12 = Permission.objects.get(codename='add_item')
    us = User.objects.create_user(
        username="test",
        password="pass",
    )
    us.user_permissions.add(p)
    us.user_permissions.add(p2)
    us.user_permissions.add(p3)
    us.user_permissions.add(p4)
    us.user_permissions.add(p5)
    us.user_permissions.add(p6)
    us.user_permissions.add(p7)
    us.user_permissions.add(p8)
    us.user_permissions.add(p9)
    us.user_permissions.add(p10)
    us.user_permissions.add(p11)
    us.user_permissions.add(p12)
    client.login(username='test', password='pass')


@pytest.fixture
def autho():
    return Author.objects.create(
    name = 'Imie',
    surname = 'Nzwisko',
    birthday = datetime.today().strftime('%Y-%m-%d'),
    nationality = 'US',
    description = 'African fiction writer'
    )


@pytest.fixture
def serie():
    return Serie.objects.create(
    name = 'Jurrasic Park',
    world = 'Jurrasic',
    nr_of_volumes = '19'
    )


@pytest.fixture
def genre():
    return Genre.objects.create(
    name = 'Wiktoriański horror'
    )


@pytest.fixture
def publisher():
    return Publisher.objects.create(
    name = 'PAX',
    city = 'Kraków',
    country = 'PL'
    )


@pytest.fixture
def item():
    item_author = Author.objects.create(
    name = 'Jonathan',
    surname = 'Carroll',
    birthday = '1949-01-26',
    nationality = 'US',
    plc_of_brth = 'None',
    plc_of_dth = 'None',
    description = 'American fiction writer'
    )

    item_user = User.objects.create_user(username='user', password='pass')

    item_genre = Genre.objects.create(
    name = 'Wiktoriański horror'
    )

    item_serie = Serie.objects.create(
    name = 'Jurrasic Park',
    world = 'Jurrasic',
    nr_of_volumes = '19'
    )

    item_publisher = Publisher.objects.create(
    name = 'PAX',
    city = 'Kraków',
    country = 'PL'
    )

    result =  Item.objects.create(
        title = 'test',
        isbn = '12121',
        cathegory = 5,
        year = 1928,
        serie = item_serie,
        volume = 4,
        notice = 'Non',
        publisher = item_publisher,
        edition = 'First',
        language = 2
    )
    result.author.set([item_author])
    result.user.set([item_user])
    result.genre.set([item_genre])
    return result

@pytest.fixture
def rate():
    return Rate.objects.create(
    user = User.objects.create_user(username='user', password='pass'),
    item = item,
    
    rate = '4'
    )