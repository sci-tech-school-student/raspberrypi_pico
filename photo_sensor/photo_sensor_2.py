from machine import Pin, PWM, ADC
import time

led = PWM(Pin(0))
led.freq(1000)
sensor = ADC(Pin(26))

while True:
    val = sensor.read_u16() * 100
    print(val)
    led.duty_u16(val)
    time.sleep(0.1)

