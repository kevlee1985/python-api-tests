import json
import requests
import variables

url = variables.base_url


def test_get():
    response = requests.post(url)
    print(f'Status code is: {response.status_code}')
    assert response.status_code == 400


def test_tc01():
    headers = {"Cookie": variables.Cookie}
    data = json.load(open('data/TC01.json', 'r'))
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    assert json_data["locationOk"] == True
    assert response.status_code == 200


def test_tc02():
    headers = {"Cookie": variables.Cookie}
    data = json.load(open('data/TC02.json', 'r'))
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    assert json_data["locationOk"] == False
    assert response.status_code == 200
