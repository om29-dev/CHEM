from machine import Pin # type: ignore
from time import sleep

#Blinking LED
def blink(a):
    led = Pin(16, Pin.OUT)
    led.off()
    sleep(a)
    led.on()
