from machine import Pin, PWM, ADC
import time

sensor = Pin(28, Pin.IN, Pin.PULL_DOWN)

while True:
    print(sensor.value())
    time.sleep(0.2)
