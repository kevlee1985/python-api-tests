import json
import requests
import variables

url = variables.base_url


# TC00 - invalid get request to URL
def test_tc00():
    response = requests.post(url)
    print(f'Status code is: {response.status_code}')
    assert response.status_code == 400


# TC01 - UK Based IP/Coordinates request
def test_tc01():
    headers = {"Cookie": variables.Cookie}
    data = json.load(open('data/TC01.json', 'r'))
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    assert json_data["locationOk"] == True
    assert response.status_code == 200


# TC02 - Non UK Based IP/Coordinates request
def test_tc02():
    headers = {"Cookie": variables.Cookie}
    data = json.load(open('data/TC02.json', 'r'))
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    assert json_data["locationOk"] == False
    assert response.status_code == 201


# TC03 - Incorrectly formatted JSON request
def test_tc03():
    headers = {"Cookie": variables.Cookie}
    data = json.load(open('data/TC03.json', 'r'))
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    assert json_data["error"] == "Bad Request"
    assert response.status_code == 400
