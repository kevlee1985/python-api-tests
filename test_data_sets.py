import requests
import pytest


data_set = [
    (1, 'Leanne Graham', 'Gwenborough', '-37.3159'),
    (2, 'Ervin Howell', 'Wisokyburgh', '-43.9509'),
    (3, 'Clementine Bauch', 'McKenziehaven', '-68.6102'),
    (4, 'Patricia Lebsack', 'South Elvis', '29.4572')
    ]


@pytest.mark.parametrize('id, name, address_city, latitude, data_set)
def test_for_names(id, name, address_city, latitude):
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    body = response.json()
    assert body['name'] == name
    assert body ['address']['city'] == address_city
    assert body['address']['geo']['lat'] == latitude
