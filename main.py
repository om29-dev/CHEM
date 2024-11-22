import network # type: ignore
import urequests
import time
from machine import ADC # type: ignore

# Variables as per need
ssid = "vivo1904"  # WiFi Network Name
password = "password"  # WiFi Network Password
hostname = "My Plant"  # Device name to be displayed
bot_token = "7622834314:AAEU4Hg0aPy3Vw-8HjHBc9tecG5dVBXAWjQ"  # Telegram bot token
chat_id = "-1002473185185"  # Chat ID of the conversation

# Initialize the sensor
sensor = ADC(0)

# Connect to WiFi
def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        time.sleep(0.5)
    print("Connected to Wi-Fi!")
    print("Hostname set to:", hostname)
    return wlan

# Verify internet connection by connecting to Google
def check_internet_connection():
    try:
        response = urequests.get("https://www.google.com")
        if response.status_code == 200:
            return True
    except:
        return False

# Function to send message to Telegram
def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}"
    try:
        response = urequests.get(url)
        if response.status_code == 200:
            print("Message sent successfully")
        else:
            print("Failed to send message")
    except:
        print("Failed to connect to Telegram")

# Setup
wlan = connect_to_wifi(ssid, password)
if check_internet_connection():
    print("Internet connection is active.")
    send_message(chat_id, "Hello")
else:
    print("No internet connection.")

# Loop
while True:
    soil_moisture = sensor.read()
    if soil_moisture < 920:
        send_message(chat_id, "Your plant needs to be watered")
    time.sleep(60)
    if soil_moisture < 920:
        send_message(chat_id, "Hurry up!")
