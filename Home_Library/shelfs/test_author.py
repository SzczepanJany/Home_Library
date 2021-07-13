import pytest

from shelfs.models import Author

@pytest.mark.django_db
def test_author_detail_view(client, author, logged_in_client):
    id = author.pk
    logged_in_client
    response = client.get(f'/detail_authr/{id}/')
    assert response.status_code == 200


# @pytest.mark.django_db
# def test_add_author_view(client, logged_in_client):
#     name = 'Jonathan'
#     surname = 'Carroll'
#     birthday = '1949-01-26'
#     nationality = 'US'
#     description = 'American fiction writer'
#     logged_in_client
#     response = client.post(
#         '/add_authr/',
#         {'name': name, 'surname': surname, 'birthday': birthday, 'nationality': nationality, 'description': description}
#     )
#     assert response.status_code == 302
#     assert Author.objects.get(name=name)

# @pytest.mark.django_db
# def test_author_list_view(author, client):
#     response = client.get('/list_authr/')
#     assert response.status_code == 200
#     product_from_context = response.context['names']
#     li1 = list(product_from_context.values_list('name', flat=True))
#     li2 = list(product_from_context.values_list('name', flat=True))
#     li2.sort()
#     assert li1 == li2