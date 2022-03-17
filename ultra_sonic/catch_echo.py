from machine import Pin, PWM, ADC
import time, utime

trigger = Pin(3, Pin.OUT)
echo = ADC(Pin(28))

trigger.value(1)

while True:
    print(echo.read_u16())
    utime.sleep(0.1)
