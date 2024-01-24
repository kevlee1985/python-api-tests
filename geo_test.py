'''

import json
import requests
from pytest_bdd import scenario, given, then

data1 = json.load(open('data/TC01.json', 'r'))


@scenario('geo_test.feature', 'UK based IP and Coordinates')
def test_geo():
    pass


@given("Player triggers geolocation API")
def geo_call(context, url):
    context.url = "https://geolocation.qa.allwyn.zenitech.co.uk/geo-check"
    print("post url: " + url)
    headers = {
        "Cookie": "AWSALB=r1gt3aqrlDiBww9wMa1gEp8oEhZ2wB1KwsVvEbeNgXlhUWwSRjdjBrJkJWdAFZsjcH5ReiGNCxsNdU9s7WPZfXUQCSoHdDDDu8VMCtfvN6MYudlxy3OmsbA/Mx6E; AWSALBCORS=r1gt3aqrlDiBww9wMa1gEp8oEhZ2wB1KwsVvEbeNgXlhUWwSRjdjBrJkJWdAFZsjcH5ReiGNCxsNdU9s7WPZfXUQCSoHdDDDu8VMCtfvN6MYudlxy3OmsbA/Mx6E"}
    data = data1
    context.response = requests.post(url, json=data, headers=headers)


#@then("Check the response status as 200")
def check_200_status(context):
    status_code = context.reponse.status_code
    assert status_code == 200
'''

