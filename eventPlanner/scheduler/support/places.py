import requests
import urllib

def get_events(address):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    key = "AIzaSyBp-Ylz26b9-GbXz2KxygPKZRfwL7-6J_8"
    headers = {'Authorization': 'Basic %s' % key}
    city = "things to do near " + address
    params = {'query': city, 'key': key}
    urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        print("nothing")

    return None
    loaded_response = response.json()





