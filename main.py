import wifi
import telegram as tg
from time import sleep as delay
import moisture

wifi.hotspot('Your Plant', 'password')
wifi.connect('vivo1904', 'password')

offset = None
while True:
    updates = tg.update(offset)
    for item in updates['result']:
        offset = item['update_id'] + 1
        chat_id = item['message']['chat']['id']
        text = item['message'].get('text')
        if text == '/start':
            message="Hello, I'm active. Use /status to know about me"
        elif text == '/status':
            message="The moisture in your plant is "+moisture.percent()+"%"
        tg.send(chat_id, message)
    delay(1)