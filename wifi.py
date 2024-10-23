import network # type: ignore

ap = network.WLAN(network.AP_IF)
sta = network.WLAN(network.STA_IF)

#Creating a Wifi Access Point
def hotspot(a,b):
    ap.active(True)
    ap.config(ssid=a, key=b)

#Connecting to a network
def connect(a,b):
    sta.active(True)
    sta.connect(a,b)
