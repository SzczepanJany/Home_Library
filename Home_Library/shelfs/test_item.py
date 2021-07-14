import pytest

from shelfs.models import Item

@pytest.mark.django_db
def test_item_detail_view(client, item, logged_in_client):
    id = item.pk
    logged_in_client
    response = client.get(f'/detail_item/{id}/')
    assert response.status_code == 200
    assert response.context['item'].name == item.name



 @pytest.mark.django_db
 def test_add_item_view(client, logged_in_client):
#     name = 'Hobbit'
#     world = 'Śródziemie'
#     nr_of_volumes = '4'
#     logged_in_client
#     response = client.post(
#         '/add_serie/',
#         {'name': name, 'world': world, 'nr_of_volumes': nr_of_volumes}
#     )
     assert response.status_code == 302
     assert Item.objects.get(name=name)
