import gc
from wifi import ap, sta

#Cleaning Memory
gc.collect()

#Clearing Wifi Activity
sta.active(False)
ap.active(False)
