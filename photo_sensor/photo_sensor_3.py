from machine import Pin, PWM, ADC
import time

servo = PWM(Pin(1))
servo.freq(50)
sensor = ADC(Pin(26))

while True:
    val = sensor.read_u16() * 20
    print(val)
    servo.duty_u16(val)
    time.sleep(0.5)

