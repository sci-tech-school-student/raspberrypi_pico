from machine import Pin, PWM, ADC
import time

led_0a = Pin(1, Pin.OUT)
led_0b = Pin(0, Pin.OUT)
led_0c = Pin(27, Pin.OUT)
led_0d = Pin(26, Pin.OUT)
led_0e = Pin(22, Pin.OUT)
led_0f = Pin(2, Pin.OUT)
led_0g = Pin(3, Pin.OUT)
led_0h = Pin(28, Pin.OUT)

_ = None
_ = [[_, _, _],
     [_, _, _],
     [_, _, _],
     [_, _, _],
     [_, _, _], ]

_dot = [[_, 0, _],
        [0, _, 0],
        [_, 0, _],
        [0, _, 0],
        [_, 0, 1], ]

_clear = [[_, 0, _],
          [0, _, 0],
          [_, 0, _],
          [0, _, 0],
          [_, 0, 0], ]

_0 = [[_, 1, _],
      [1, _, 1],
      [_, 0, _],
      [1, _, 1],
      [_, 1, 0], ]

_1 = [[_, 0, _],
      [0, _, 1],
      [_, 0, _],
      [0, _, 1],
      [_, 0, 0], ]

_2 = [[_, 1, _],
      [0, _, 1],
      [_, 1, _],
      [1, _, 0],
      [_, 1, 0], ]

_3 = [[_, 1, _],
      [0, _, 1],
      [_, 1, _],
      [0, _, 1],
      [_, 1, 0], ]

_4 = [[_, 0, _],
      [1, _, 1],
      [_, 1, _],
      [0, _, 1],
      [_, 0, 0], ]

_5 = [[_, 1, _],
      [1, _, 1],
      [_, 1, _],
      [1, _, 1],
      [_, 1, 0], ]

_6 = [[_, 1, _],
      [1, _, 0],
      [_, 1, _],
      [1, _, 1],
      [_, 1, 0], ]

_7 = [[_, 1, _],
      [1, _, 1],
      [_, 0, _],
      [0, _, 1],
      [_, 0, 0], ]

_8 = [[_, 1, _],
      [1, _, 1],
      [_, 1, _],
      [1, _, 1],
      [_, 1, 0], ]

_9 = [[_, 1, _],
      [1, _, 1],
      [_, 1, _],
      [0, _, 1],
      [_, 0, 0], ]

nums = [_0, _1, _2, _3, _4, _5, _6, _7, _8, _9]


def digit(nums):
    led_0a.value(nums[0][1])
    led_0b.value(nums[1][2])
    led_0c.value(nums[3][2])
    led_0d.value(nums[4][1])
    led_0e.value(nums[3][0])
    led_0f.value(nums[1][0])
    led_0g.value(nums[2][1])
    led_0h.value(nums[4][2])


while True:
    for num in nums:
        digit(num)
        time.sleep(1)
        digit(_clear)
