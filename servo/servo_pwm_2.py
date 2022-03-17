from machine import Pin, PWM
import time

# pinとうろく
servo_1 = PWM(Pin(1))

# 1秒間に50回切り替える
servo_1.freq(50)

# max_duty_u16 = 65025
_0 = 1500
_180 = 8500

while True:
    servo_1.duty_u16(_0)
    time.sleep(2)
    servo_1.duty_u16(_180)
    time.sleep(2)

