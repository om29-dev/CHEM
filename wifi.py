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

#Connecting to a Wifi Network
def connect(a,b):
    sta.active(True)
    sta.connect(ssid=a, key=b)