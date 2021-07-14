import pytest

from shelfs.models import Genre

@pytest.mark.django_db
def test_genre_detail_view(client, genre, logged_in_client):
    id = genre.pk
    logged_in_client
    response = client.get(f'/detail_genre/{id}/')
    assert response.status_code == 200


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
