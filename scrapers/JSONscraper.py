from urllib.request import urlopen
import json


def fetch_data(url):

    data = json.load(urlopen(url))
    return data




