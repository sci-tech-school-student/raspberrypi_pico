from machine import Pin
import time

led = Pin(25, Pin.OUT)
led_2 = Pin(1, Pin.OUT)
led_3 = Pin(5, Pin.OUT)
led_4 = Pin(9, Pin.OUT)

button = Pin(15, Pin.IN, Pin.PULL_DOWN)
button_2 = Pin(14, Pin.IN, Pin.PULL_DOWN)
button_3 = Pin(16, Pin.IN, Pin.PULL_DOWN)


def swhitch_led(LED, Button):
    if Button.value():
        LED.value(1)
        led_2.value(1)
        led_3.value(1)
        led_4.value(1)
    else:
        LED.value(0)
        led_2.value(0)
        led_3.value(0)
        led_4.value(0)


while True:
    swhitch_led(led, button)
    swhitch_led(led_2, button_2)
    swhitch_led(led_3, button_3)
