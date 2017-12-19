__author__ = '38720'
# coding=utf-8

import pygame, requests
import json

ID = '10523179'
KEY = 'pFuXmDjbfQxFKResdKPlqexU'
SECRET_KEY = 'd6835ddee8127e5ae732180b465b41a8'
get_token_url = 'https://aip.baidubce.com/oauth/2.0/token'
URL = 'http://tsn.baidu.com/text2audio'

data = {
    'tex': '你好 世界 # > hello world',
    'tok': SECRET_KEY,
    'cuid': '1337372',
    'ctp': '1',
    'lan': 'zh',
}
token_data = {
    'grant_type':'client_credentials',
    'client_id': '10523179',
    'client_secret':'d6835ddee8127e5ae732180b465b41a8',
}
headers = ('Content-Type', 'application/json; charset=UTF-8')

r = requests.post(url=get_token_url, data=token_data)
print(type(r))
print(r.headers)
print(r.status_code)
