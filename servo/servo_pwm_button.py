from machine import Pin, PWM
import time

# pinとうろく
led = Pin(25, Pin.OUT)
servo_1 = PWM(Pin(1))
button_1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button_2 = Pin(14, Pin.IN, Pin.PULL_DOWN)
button_3 = Pin(15, Pin.IN, Pin.PULL_DOWN)

# 1秒間に50回切り替える
servo_1.freq(50)

# max_duty_u16 = 65025
_0 = 1500
_45 = 3300
_90 = 5000
_135 = 6800
_180 = 8500
val = _0

led.value(1)
while True:
    if button_1.value() == True & button_2.value() == True:
        val = _45
        print(val)
    elif button_2.value() == True & button_3.value() == True:
        val = _135
        print(val)
    elif button_1.value() == True:
        val = _0
        print(val)
    elif button_2.value() == True:
        val = _90
        print(val)
    elif button_3.value() == True:
        val = _180
        print(val)
    else:
        pass
    servo_1.duty_u16(val)
    time.sleep(0.2)
