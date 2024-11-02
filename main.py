import wifi
import led

wifi.hotspot('Your Plant', 'password')
wifi.connect('vivo1904', 'password')

led.blink(1000)
