import machine
import  time

led = machine.Pin(25, machine.Pin.OUT)

# ずっとと同じ
while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)

