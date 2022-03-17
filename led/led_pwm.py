from machine import Pin, PWM
import time

# pinとうろく
led = PWM(Pin(1))

# 1秒間に1000回切り替える
led.freq(50)

while True:
    # 2進数表現 1111111000000000
    for i in range( 0,65025, 100):
        led.duty_u16(i)
        print(i)
        time.sleep(0.0001)

    for i in range(65025, 0, -100):
        led.duty_u16(i)
        print(i)
        time.sleep(0.0001)

    led.duty_u16(0)
    time.sleep(1)