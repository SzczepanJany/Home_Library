import pytest

from shelfs.models import Author

@pytest.mark.django_db
def test_author_detail_view(client, autho, logged_in_client):
    logged_in_client
    id = autho.id
    response = client.get(f'/detail_authr/{id}/')
    assert response.status_code == 200


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
