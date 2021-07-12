import pytest

from shelfs.models import Author, Serie

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
        Author.objects.create(name=name, world='test')