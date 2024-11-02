from machine import Pin # type: ignore
from time import sleep_ms as delay

#Blinking LED
def blink(a,b):
    led = Pin(16, Pin.OUT)
    for i in range(0,b):
        led.off()
        delay(a)
        led.on()
