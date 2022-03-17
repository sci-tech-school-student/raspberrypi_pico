from machine import Pin
import time

led = Pin(1, Pin.OUT)

# When pushed, button.value() returns False.
button_1 = Pin(15, Pin.IN, Pin.PULL_DOWN)
is_on_1 = True


def switch_led(led, button, is_on):
    ex_val = button.value()
    time.sleep(0.1)
    if button.value() == True and ex_val == False:
        if is_on == True:
            led.value(1)
            is_on = False
        elif is_on == False:
            led.value(0)
            is_on = True
        # time.sleep(0.3)
    return is_on


while True:
    is_on_1 = switch_led(led, button_1, is_on_1)
