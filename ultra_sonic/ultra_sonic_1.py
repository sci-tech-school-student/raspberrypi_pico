from machine import Pin
import utime

echo = Pin(2, Pin.IN)
trigger = Pin(3, Pin.OUT)


def ultra():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()

    signal_on = 0
    signal_off = 0
    while echo.value() == False:
        signal_off = utime.ticks_us()
    while echo.value() == True:
        signal_on = utime.ticks_us()

    time_passed = signal_on - signal_off
    distance = (time_passed * 0.0343) / 2
    print("The distance from object is ", distance, "cm")


while True:
    ultra()
    utime.sleep(0.2)
