import requests

url = "https://booking-com.p.rapidapi.com/v1/hotels/search"

querystring = {"order_by": "price",
               "checkout_date": "2024-05-20",
               "filter_by_currency": "GBP", "locale": "en-gb", "units": "metric", "dest_id": "-2601889",
               "dest_type": "city", "adults_number": "2", "room_number": "1", "checkin_date": "2024-05-19",
               "include_adjacency": "true", "page_number": "0", "children_number": "3",
               "categories_filter_ids": "class::2,class::4,free_cancellation::1", "children_ages": "9,7,4"}

headers = {
    "X-RapidAPI-Key": "b2ae21ad77mshbc9202b20e9e331p1dfc11jsn0f075a40f3d3",
    "X-RapidAPI-Host": "booking-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
body = response.json()
print(body['primary_count'])

#print(response.json())
'''

url = "https://booking-com.p.rapidapi.com/v1/static/cities"

querystring = {"page":"0","name":"london","country":"gb"}

headers = {
	"X-RapidAPI-Key": "b2ae21ad77mshbc9202b20e9e331p1dfc11jsn0f075a40f3d3",
	"X-RapidAPI-Host": "booking-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
'''
