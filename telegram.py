import requests
import json

# Replace with your bot's token
BOT_TOKEN = '7622834314:AAEU4Hg0aPy3Vw-8HjHBc9tecG5dVBXAWjQ'
# Telegram API URL
URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'

def send_message(chat_id, text):
    url = URL + 'sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response

def handle_updates():
    url = URL + 'getUpdates'
    response = requests.get(url)
    updates = response.json()
    for update in updates['result']:
        if 'message' in update:
            message = update['message']
            chat_id = message['chat']['id']
            text = message.get('text', '')
            if text == '/start':
                send_message(chat_id, 'Hello! Welcome to the Telegram Bot.')