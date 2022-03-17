from machine import Pin, PWM
import time

# pinとうろく
servo_1 = PWM(Pin(1))

# 1秒間に50回切り替える
servo_1.freq(50)

max_duty_u16 = 65025


while True:
    for i in range(0, max_duty_u16, 100):
            print(i)
            servo_1.duty_u16(i)
            time.sleep(0.05)

    for i in range(max_duty_u16, 0, -100):
            print(i)
            servo_1.duty_u16(i)
            time.sleep(0.05)

