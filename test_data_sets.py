import requests
import pytest


data_set = [
    (1, 'Leanne Graham', 'Gwenborough'),
    (2, 'Ervin Howell', 'Wisokyburgh'),
    ]


@pytest.mark.parametrize('id, name, address_city', data_set)
def test_for_names(id, name, address_city):
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    body = response.json()
    assert body['name'] == name
    assert body ['address']['city'] == address_city
