import pytest

from shelfs.models import Serie

@pytest.mark.django_db
def test_serie_detail_view(client, serie):
    id = serie.pk
    client.login(username='admin', password='admin')
    response = client.get(f'/detail_serie/{id}/')
    # assert response.status_code == 200
    assert response.status_code == 302

@pytest.mark.django_db
def test_add_serie_view(client):
    name = 'Hobbit'
    world = 'Śródziemie'
    nr_of_volumes = '4'
    response = client.post(
        '/add_serie/',
        {'name': name, 'world': world, 'nr_of_volumes': nr_of_volumes}
    )
    assert response.status_code == 302
    # assert Serie.objects.get(name=name)

# @pytest.mark.django_db
# def test_serie_list_view(serie, client):
#     response = client.get('/list_serie/')
#     assert response.status_code == 200
#     product_from_context = response.context['names']
#     li1 = list(product_from_context.values_list('name', flat=True))
#     li2 = list(product_from_context.values_list('name', flat=True))
#     li2.sort()
#     assert li1 == li2