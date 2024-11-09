import requests as req
from time import sleep as delay
import json
from config import TOKEN

URL = f'https://api.telegram.org/bot{TOKEN}'

def update(offset=None):
    params = {'timeout': 100, 'offset': offset}
    response = req.get(f'{URL}/getUpdates', params=params)
    return response.json()

def send(chat_id, text):
    params = {'chat_id': chat_id, 'text': text}
    req.post(f'{URL}/sendMessage', params=params)