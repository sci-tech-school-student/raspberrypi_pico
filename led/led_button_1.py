from machine import Pin
import time

led = Pin(25, Pin.OUT)
led_2 = Pin(1, Pin.OUT)
led_3 = Pin(5, Pin.OUT)

# When pushed, button.value() returns False.
button = Pin(15, Pin.IN, Pin.PULL_DOWN)
button_2 = Pin(14, Pin.IN, Pin.PULL_DOWN)
button_3 = Pin(16, Pin.IN, Pin.PULL_DOWN)
# button_2 = Pin(14, Pin.IN, Pin.PULL_UP)


while True:
    if button.value():
        led.value(1)
    else:
        led.value(0)

    if button_2.value():
        led_2.value(1)
    else:
        led_2.value(0)

    if button_3.value():
        led_3.value(1)
    else:
        led_3.value(0)
