import gc
import network # type: ignore

#Cleaning Memory
gc.collect()

#Clearing Wifi Activity
sta = network.WLAN(network.STA_IF)
sta.active(False)
ap = network.WLAN(network.AP_IF)
ap.active(False)
