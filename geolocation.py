import json

import requests

# base_url:
base_url = "https://geolocation.qa.allwyn.zenitech.co.uk/geo-check"

# COOKIE:
Cookie = "AWSALB=r1gt3aqrlDiBww9wMa1gEp8oEhZ2wB1KwsVvEbeNgXlhUWwSRjdjBrJkJWdAFZsjcH5ReiGNCxsNdU9s7WPZfXUQCSoHdDDDu8VMCtfvN6MYudlxy3OmsbA/Mx6E; AWSALBCORS=r1gt3aqrlDiBww9wMa1gEp8oEhZ2wB1KwsVvEbeNgXlhUWwSRjdjBrJkJWdAFZsjcH5ReiGNCxsNdU9s7WPZfXUQCSoHdDDDu8VMCtfvN6MYudlxy3OmsbA/Mx6E"


def test_get():
    url = base_url
    response = requests.post(url)
    assert response.status_code == 400


def test_kev():
    url = base_url
    print("post url: " + url)
    headers = {"Cookie": Cookie}
    data = {
        "ipAddress": "130.185.117.161",
        "coordinates": {
            "latitude": -1,
            "longitude": 2.9916
        }
    }
    response = requests.post(url, json=data, headers=headers)
    status = response.status_code
    print("status code is: " + str(status))
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print(json_str)
    assert "locationOk" in json_data
    assert json_data["locationOk"] == True
