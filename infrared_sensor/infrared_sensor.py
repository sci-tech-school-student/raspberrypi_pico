from machine import Pin, PWM, ADC
import time

infrared_led_0 = Pin(0, Pin.OUT)
# infrared_sensor_2 = Pin(15, Pin.IN, Pin.PULL_DOWN)
infrared_sensor_2 = ADC(Pin(26))

infrared_led_0.value(1)
counter = 0
while True:
    # if infrared_sensor_2.value():
    #     print('get input')
    # else:
    #     print('no input')
    print(infrared_sensor_2.read_u16())
    time.sleep(0.1)

    counter += 1
    if 0 <= counter % 50 <= 25:
        infrared_led_0.value(1)
        if counter % 50 == 0:
            print('***** 0')
    else:
        infrared_led_0.value(0)
        if counter % 50 == 26:
            print('***** 26')
