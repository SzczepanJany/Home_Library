import pytest

from shelfs.models import Serie

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
