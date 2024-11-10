import wifi
from telegram import handle_updates
from time import sleep as delay
import moisture


wifi.hotspot('Your Plant', 'password')
wifi.connect('vivo1904', 'password')

if wifi.check():
    while True:
        handle_updates()