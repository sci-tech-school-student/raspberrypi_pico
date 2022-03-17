from machine import Pin
import time

# とうろく
led = Pin(25, Pin.OUT)
led_2 = Pin(1, Pin.OUT)
led_3 = Pin(5, Pin.OUT)
led_4 = Pin(9, Pin.OUT)
led_5 = Pin(13, Pin.OUT)
byo = 0.2

"""
入力 input
出力 output
"""


# 出力=電気を出す
# 入力=電気を入れる(うけとる)

# def 関数
# カッコの中の変数：引数

def leds(n1, n2, n3, n4, n5):
    led.value(n1)
    led_2.value(n2)
    led_3.value(n3)
    led_4.value(n4)
    led_5.value(n5)
    time.sleep(byo)


# ずっと
while True:
    leds(1, 0, 0, 0, 0)
    leds(0, 1, 0, 0, 0)
    leds(0, 0, 1, 0, 0)
    leds(0, 0, 0, 1, 0)
    leds(0, 0, 0, 0, 1)
    leds(0, 0, 0, 1, 0)
    leds(0, 0, 1, 0, 0)
    leds(0, 1, 0, 0, 0)


