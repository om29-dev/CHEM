from machine import Pin # type: ignore
from time import sleep_ms as delay

#Blinking LED
def blink(a):
    led = Pin(16, Pin.OUT)
    led.off()
    delay(a)
    led.on()
