import pytest

from shelfs.models import Author

@pytest.mark.django_db
def test_author_detail_view(client, author):
    id = author.id
    response = client.get(f'/detail_authr/{id}/')
    assert response.status_code == 200
    # assert response.context['name'] == author.name
    # assert response.context['surname'] == author.surname
    # assert response.context['birthday'] == author.birthday
    # assert response.context['nationality'] == author.nationality
    # assert response.context['description'] == author.description


# @pytest.mark.django_db
# def test_add_author_view(client):
#     name = 'Jonathan'
#     surname = 'Carroll'
#     birthday = '1949-01-26'
#     nationality = 'US'
#     description = 'American fiction writer'
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