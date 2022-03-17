from machine import Pin, PWM
import time

# pinとうろく
led = Pin(25, Pin.OUT)

servo_1 = PWM(Pin(0))
servo_2 = PWM(Pin(1))

button_1 = Pin(19, Pin.IN, Pin.PULL_DOWN)
button_2 = Pin(18, Pin.IN, Pin.PULL_DOWN)
button_3 = Pin(17, Pin.IN, Pin.PULL_DOWN)
button_4 = Pin(16, Pin.IN, Pin.PULL_DOWN)

# 1秒間に50回切り替える
servo_1.freq(50)

# max_duty_u16 = 65025
# _0 = 1500
# _45 = 3300
# _90 = 5000
# _135 = 6800
# _180 = 8500

deg_1 = 5000
deg_2 = 5000
val = 200

led.value(1)
while True:
    if button_1.value() == True:
        deg_1 += val
        print(deg_1)
    elif button_2.value() == True:
        deg_1 -= val
        print(deg_1)
    elif button_3.value() == True:
        deg_2 += val
        print(deg_2)
    elif button_4.value() == True:
        deg_2 -= val
        print(deg_2)
    servo_1.duty_u16(deg_1)
    servo_2.duty_u16(deg_2)
    time.sleep(0.2)

