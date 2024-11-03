import network # type: ignore

ap = network.WLAN(network.AP_IF)
sta = network.WLAN(network.STA_IF)

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
        print("Wifi Hotspot Created Successfully with IP Address:", ip)
    else:
        print("Error:W1")

#Connecting to a Wifi Network
def connect(a,b):
    sta.active(True)
    sta.connect(ssid=a, key=b)
    if sta.isconnected():
        print("Connected to Wifi Successfully")
    else:
        print("Error:W2")