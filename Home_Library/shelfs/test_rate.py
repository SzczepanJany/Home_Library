import pytest

from shelfs.models import Rate, Item, User

@pytest.mark.django_db
def test_rate_detail_view(client, rate, logged_in_client):
    id = rate.pk
    logged_in_client
    response = client.get(f'/detail_rate/{id}/')
    assert response.status_code == 200
    

@pytest.mark.django_db
def test_add_rate_view(client, logged_in_client):
    item = Item.objects.create()
    user = User.objects.create_user()
    rate = '4'
    response = client.post(
        '/add_rate/',
        {'item': item, 'user': user, 'rate': rate}
    )
    assert response.status_code == 302
    assert Rate.objects.get(rate=rate)
    