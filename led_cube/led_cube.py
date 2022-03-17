from machine import Pin, PWM, ADC
import time

leds = [Pin(i, Pin.OUT) for i in range(12)]
green = Pin(25, Pin.OUT)

leds[9].value(1)
leds[10].value(1)
leds[11].value(1)

while True:
    # leds[0].value(1)
    # green.value(1)
    # time.sleep(0.1)
    # leds[0].value(0)
    # green.value(0)
    # time.sleep(0.1)

    for i in range(12):
        leds[i].value(1)
        time.sleep(0.1)
        for j in range(9,-1,-1):
            leds[j].value(0)
            time.sleep(0.1)
