from machine import Pin
import time

led = Pin(25, Pin.OUT)

# When pushed, button.value() returns False.
button_1 = Pin(15, Pin.IN, Pin.PULL_DOWN)
is_on_1 = True

while True:
    ex_val = button_1.value()
    time.sleep(0.1)
    if button_1.value() and ex_val == False:
        if is_on_1 == True:
            led.value(1)
            is_on_1 = False

        elif is_on_1 == False:
            led.value(0)
            is_on_1 = True
