# This file is executed on every boot (including wake-boot from deepsleep)
import webrepl
webrepl.start()

import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('ssid', 'password')
while wlan.isconnected() == False:
  pass

print('Connection successful')
print(wlan.ifconfig())

import machine
machine.freq(240000000)
machine.freq()

# import esp
# esp.osdebug(None)

import gc
gc.collect()