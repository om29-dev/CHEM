from machine import Pin # type: ignore
from time import sleep_ms as delay
led = Pin(16, Pin.OUT)

#Blinking LED
def blink(a,b,c):
    for i in range(0,a):
        led.off()
        delay(b)
        led.on()
        delay(c)
