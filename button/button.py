from machine import Pin
import time

button = Pin(15, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        print('Push')
    else:
        print('Release')
    time.sleep(0.2)




