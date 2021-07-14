import pytest

from shelfs.models import Author, Genre, Serie, Publisher

@pytest.mark.django_db
def test_author_detail_view(client, autho, logged_in_client):
    logged_in_client
    id = autho.id
    response = client.get(f'/detail_authr/{id}/')
    assert response.status_code == 200
    assert response.context['author'].name == autho.name



@pytest.mark.django_db
def test_add_author_view(client, logged_in_client):
    name = 'Jonathan'
    surname = 'Carroll'
    birthday = '1949-01-26'
    nationality = 'US'
    plc_of_brth = 'None'
    plc_of_dth = 'None'
    description = 'American fiction writer'
    logged_in_client
    #breakpoint()
    response = client.post(
        '/add_authr/',
        {'name': name, 'surname': surname, 'birthday': birthday, 'nationality': nationality, 'plc_of_brth': plc_of_brth,'plc_of_dth': plc_of_dth,'description': description}
    )
    assert response.status_code == 302
    assert Author.objects.get(name=name)


@pytest.mark.django_db
def test_genre_detail_view(client, genre, logged_in_client):
    id = genre.pk
    logged_in_client
    response = client.get(f'/detail_genre/{id}/')
    assert response.status_code == 200
    assert response.context['genre'].name == genre.name


@pytest.mark.django_db
def test_add_genre_view(client, logged_in_client):
    name = 'Powieść szufladkowa'
    logged_in_client
    response = client.post(
        '/add_genre/',
        {'name': name}
    )
    assert response.status_code == 302
    assert Genre.objects.get(name=name)


@pytest.mark.django_db
def test_serie_detail_view(client, serie, logged_in_client):
    id = serie.pk
    logged_in_client
    response = client.get(f'/detail_serie/{id}/')
    assert response.status_code == 200
    assert response.context['serie'].name == serie.name


@pytest.mark.django_db
def test_add_serie_view(client, logged_in_client):
    name = 'Hobbit'
    world = 'Śródziemie'
    nr_of_volumes = '4'
    logged_in_client
    response = client.post(
        '/add_serie/',
        {'name': name, 'world': world, 'nr_of_volumes': nr_of_volumes}
    )
    assert response.status_code == 302
    assert Serie.objects.get(name=name)



@pytest.mark.django_db
def test_publisher_detail_view(client, publisher, logged_in_client):
    id = publisher.pk
    logged_in_client
    response = client.get(f'/detail_publish/{id}/')
    assert response.status_code == 200
    assert response.context['publisher'].name == publisher.name


@pytest.mark.django_db
def test_add_publisher_view(client, logged_in_client):
    name = 'Pascal'
    city = 'Olsztyn'
    country = 'DE'
    logged_in_client
    response = client.post(
        '/add_publish/',
        {'name': name, 'city': city, 'country': country}
    )
    assert response.status_code == 302
    assert Publisher.objects.get(name=name)


@pytest.mark.django_db
def test_item_detail_view(client, item, logged_in_client):
    id = item.pk
    logged_in_client
    response = client.get(f'/detail_item/{id}/')
    assert response.status_code == 200
    assert response.context['item'].title == item.title
