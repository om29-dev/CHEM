#Cleaning Memory
import gc
import machine # type: ignore
import time
gc.collect()

#Clearing Wifi Activity
import network # type: ignore
sta = network.WLAN(network.STA_IF)
sta.active(False)
ap = network.WLAN(network.AP_IF)
ap.active(False)

#Creating a Wifi Access Point
def ap(a,b):
    ap.active(True)
    ap.config(ssid=a, key=b)

#Connecting to a network
def sta(a,b):
    sta.active(True)
    sta.connect(a,b)

# Getting the analog pin
adc = machine.ADC(0)

# Function to read soil moisture
def moisture():
    value = adc.read()
    # Convert analog value to percentage
    percent = 100 - ((value / 1023.0) * 100)
    return percent

#Blinking LED
def led(a):
    led = machine.Pin(16, machine.Pin.OUT)
    led.off()
    time.sleep(a)
    led.on()