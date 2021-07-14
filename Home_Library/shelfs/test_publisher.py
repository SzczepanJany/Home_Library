import pytest

from shelfs.models import Publisher

@pytest.mark.django_db
def test_publisher_detail_view(client, publisher, logged_in_client):
    id = publisher.pk
    logged_in_client
    response = client.get(f'/detail_publish/{id}/')
    assert response.status_code == 200


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
