import gc
from wifi import ap, sta
from led import blink

#Cleaning Memory
gc.collect()

#Clearing Wifi Activity
ap.active(False)
sta.active(False)

blink(2,0.5,0.1)