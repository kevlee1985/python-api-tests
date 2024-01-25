import json
import requests
import variables

url = variables.shop_base_url


def test_get_request():
    response = requests.get(url + '/2')
    json_data = json.loads(response.content)
    assert json_data["title"] == "Mens Casual Premium Slim Fit T-Shirts "
    assert response.status_code == 200


def test_post_product():
    data = json.load(open('data/shop_data/item_1.json', 'r'))
    response = requests.post(url, json=data)
    json_data = json.loads(response.content)
    assert json_data["id"] > 0
    print(f'Response body:{json.dumps(response.json(), indent=3)}')

