import gc
from wifi import ap, sta
from led import blink

#Cleaning Memory
gc.collect()

#Clearing Wifi Activity
sta.active(False)
ap.active(False)

blink(2,200,200)