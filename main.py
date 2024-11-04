import wifi

wifi.hotspot('Your Plant', 'password')
wifi.connect('vivo1904', 'password')


import requests
import time

TOKEN = 'YOUR_BOT_TOKEN'
URL = f'https://api.telegram.org/bot{TOKEN}'

def get_updates(offset=None):
    params = {'timeout': 100, 'offset': offset}
    response = requests.get(f'{URL}/getUpdates', params=params)
    return response.json()

def send_message(chat_id, text):
    params = {'chat_id': chat_id, 'text': text}
    requests.post(f'{URL}/sendMessage', params=params)

def main():
    offset = None
    while True:
        updates = get_updates(offset)
        for item in updates['result']:
            offset = item['update_id'] + 1
            chat_id = item['message']['chat']['id']
            text = item['message'].get('text')

            if text == '/start':
                send_message(chat_id, "Hello, I'm active. Use /status to know about me")

        time.sleep(1)

if __name__ == '__main__':
    main()