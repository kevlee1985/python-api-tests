import requests
import json


# # response = requests.get('https://api.zippopotam.us/GB/LL13')
# # print(f'Response status code:{response.status_code}')
# # print(f'Response headers:{response.headers}')
# # print(f'Response body:{json.dumps(response.json(), indent=3)}')
#
#
# data = {
#     'place name': 'Amsterdam',
#     'country': 'The Netherlands'
# }
#
# another_response = requests.post('https://api.zippopotam.us', json=data)
# print(f'Response status code:{another_response.status_code}')
# print(f'Request payload sent: {another_response.request.body}')

def extract_value_pair(data, key1, key2):
    key_value = data[key1]
    key_value2 = data[key2]
    print(key1 + f' is {key_value} and ' + key2 + f' is {key_value2}')


response = requests.get('https://jsonplaceholder.typicode.com/users/2')
extract = requests.get('https://jsonplaceholder.typicode.com/users/2').json()
print(f'Response status code: {response.status_code}')
# print(f'Response headers:{response.headers}')
# print(f'Response body:{json.dumps(response.json(), indent=3)}')
extract_value_pair(extract, 'name', 'phone')
extract_value_pair(extract, 'name', 'username')
