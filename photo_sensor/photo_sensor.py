from machine import Pin, PWM, ADC
import time

sensor = ADC(Pin(26))

while True:
    print(sensor.read_u16())
    time.sleep(1)
