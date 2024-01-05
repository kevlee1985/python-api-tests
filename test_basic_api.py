import string

import requests


def test_status_code():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    assert response.status_code == 200
    print(f'Response code is: {response.status_code}')


def test_status_code2():
    response = requests.get('https://jsonplaceholder.typicode.com/99999999')
    assert response.status_code == 404
    print(f'Response code is: {response.status_code}')


def test_assert_body_element():
    response = requests.get('https://jsonplaceholder.typicode.com/users/7')
    body = response.json()
    assert body['name'] == 'Kurtis Weissnat'
