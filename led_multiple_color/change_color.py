from machine import Pin, PWM, ADC
import time

led_0 = PWM(Pin(1))
led_1 = PWM(Pin(2))
led_2 = PWM(Pin(3))

led_0.freq(1000)
led_1.freq(1000)
led_2.freq(1000)


led_1.duty_u16(10000)
led_2.duty_u16(10000)

while True:
    for i in range(0,60000,1000):
        led_0.duty_u16(i)
        time.sleep(0.1)



