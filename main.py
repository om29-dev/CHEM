import wifi
import telegram as tg

wifi.hotspot('Your Plant', 'password')
wifi.connect('vivo1904', 'password')

def main():
    offset = None
    while True:
        updates = tg.update(offset)
        for item in updates['result']:
            offset = item['update_id'] + 1
            chat_id = item['message']['chat']['id']
            text = item['message'].get('text')

            if text == '/start':
                send_message(chat_id, "Hello, I'm active. Use /status to know about me")

        time.sleep(1)

if __name__ == '__main__':
    main()