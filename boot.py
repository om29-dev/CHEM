#Cleaning Memory
import gc
gc.collect()

#Clearing Wifi Activity
import network # type: ignore
sta = network.WLAN(network.STA_IF)
sta.active(False)
ap = network.WLAN(network.AP_IF)
ap.active(False)

#Creating a Wifi Access Point
ap.active(True)
ap.config(ssid="Your Plant", key="password")

#Connecting to my network
sta.active(True)
sta.connect('vivo1904','password')

#Blinking LED
from machine import Pin # type: ignore
from time import sleep
led = Pin(16, Pin.OUT)
led.off()
sleep(1)
led.on()