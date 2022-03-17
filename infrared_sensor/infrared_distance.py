from machine import Pin, PWM, ADC
import time

motor = Pin(2, Pin.OUT)
infrared_sensor = ADC(Pin(27))

while True:
    val = infrared_sensor.read_u16()
    print(val)
    if val >= 60000:
        motor.value(0)
    elif val <= 3000:
        motor.value(1)
    time.sleep(0.1)

