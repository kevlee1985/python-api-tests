import requests

query = """
{
    company {
    ceo
    coo
    name
    }
}
"""

payload = {'query': query}


def test_graphql():
    response = requests.post('https://api.spacex.land/graphql/', json=payload)
    assert response.status_code == 200
