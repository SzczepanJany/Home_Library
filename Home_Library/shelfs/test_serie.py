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

@pytest.mark.django_db
def test_serie_list_view(series, client):
    response = client.get('')
    assert response.status_code == 200
    product_from_context = response.context['items']
    li1 = list(product_from_context.values_list('name', flat=True))
    li2 = list(product_from_context.values_list('name', flat=True))
    li2.sort()
    assert li1 == li2