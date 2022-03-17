from machine import ADC, Pin, PWM
import time

led = PWM(Pin(1))
led.freq(1000)
photo_sensor = ADC(Pin(26))

while True:
    val = photo_sensor.read_u16()
    led.duty_u16(val * 10)
    time.sleep(0.1)
