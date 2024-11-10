import gc
from wifi import ap, sta
from led import blink

#Cleaning Memory
gc.collect()

#Clearing Wifi Activity
ap.active(False)
sta.active(False)

#Indicates Successful Boot
blink(1,1,1)