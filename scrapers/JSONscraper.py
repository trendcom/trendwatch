import urllib.request
import json


def fetch_data(url):

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
    return data





