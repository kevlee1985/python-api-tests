import json
import requests
import variables

url = variables.base_url


def post_call(file_name: str):
    headers = {"Cookie": variables.Cookie}
    data = json.load(open('data/' + file_name + '.json', 'r'))
    response = requests.post(url, json=data, headers=headers)
    return response


# TC00 - invalid get request to URL
def test_tc00():
    response = requests.post(url)
    print(f'Status code is: {response.status_code}')
    assert response.status_code == 400


# TC01 - UK Based IP/Coordinates request
def test_tc01():
    response = post_call("TC01")
    json_data = json.loads(response.content)
    assert json_data["locationOk"] == True
    assert response.status_code == 200


# TC02 - Non UK Based IP/Coordinates request
def test_tc02():
    response = post_call("TC02")
    json_data = json.loads(response.content)
    assert json_data["locationOk"] == False
    assert response.status_code == 200


# TC03 - Incorrectly formatted JSON request
def test_tc03():
    response = post_call("TC03")
    json_data = json.loads(response.content)
    assert json_data["error"] == "Bad Request"
    assert response.status_code == 400
