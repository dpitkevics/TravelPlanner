from urllib.parse import urlencode
from collections import OrderedDict
import requests
import json


def vk_api(method, params=None, token=None):
    try:
        if params is None:
            params = {}

        if token is not None:
            params['access_token'] = token

        params['lang'] = 'en'
        url_query = urlencode(OrderedDict(params))
        url = "https://api.vk.com/method/%s?%s" % (method, url_query)

        data = requests.get(url)
        decoded_data = json.loads(data.text)

        return decoded_data
    except NameError as e:
        print(e)