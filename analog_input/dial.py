from machine import Pin, PWM, ADC
import time

dial = ADC(Pin(27))
led = PWM(Pin(0))
led.freq(1000)

while True:
    val = dial.read_u16()
    print(val)
    led.duty_u16(val)
    time.sleep(0.1)
