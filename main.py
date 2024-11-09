import wifi
import telegram as tg
from time import sleep as delay
import moisture

wifi.hotspot('Your Plant', 'password')
wifi.connect('vivo1904', 'password')
a=moisture.percent()

offset = None
while True:
    updates = tg.update(offset)
    for item in updates['result']:
        offset = item['update_id'] + 1
        chat_id = item['message']['chat']['id']
        if a<20:
            message="Your Plant needs to be watered"
        text = item['message'].get('text')
        if text == '/start':
            message="Hello, I'm active. Use /status to know about me"
        elif text == '/status':
            message="The moisture in your plant is "+a+"%"
        else:
            message="Invalid command"
        tg.send(chat_id, message)
    delay(1)