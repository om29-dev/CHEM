import network # type: ignore

ap = network.WLAN(network.AP_IF)
sta = network.WLAN(network.STA_IF)

x = "Wifi Hotspot"
y = "Connected to Wifi"

#Scanning nearby Wifi Networks
def scan():
    sta.active(True)
    a=sta.scan()
    sta.active(False)
    return a

#Creating a Wifi Access Point
def hotspot(a,b):
    ap.active(True)
    ap.config(ssid=a, key=b)
    if ap.active():
        ip=ap.ifconfig()[0]
        print(x, "Created Successfully with IP Address:", ip)
    else:
        print("Unable to create", x)

#Connecting to a Wifi Network
def connect(a,b):
    sta.active(True)
    sta.connect(ssid=a, key=b)
    if sta.isconnected():
        print(y, "Sucessfully")
    else:
        print("Couldn't", y)