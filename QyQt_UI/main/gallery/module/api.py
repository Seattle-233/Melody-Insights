# coding:utf-8

import requests

host = 'http://localhost:3000'

def api_get(api):
    url = host + api
    print(f'URL is {url}')

    response = requests.get(url)
    return response
