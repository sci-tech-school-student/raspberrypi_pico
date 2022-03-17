from machine import Pin, PWM, ADC
import time

buzzer = PWM(Pin(15))
buzzer.freq(1000)

while True:
    buzzer.duty_u16(10000)
    time.sleep(1)
    buzzer.duty_u16(0)
    time.sleep(1)
    buzzer.duty_u16(30000)
    time.sleep(1)
