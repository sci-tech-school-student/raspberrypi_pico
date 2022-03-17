from machine import Pin

leds = [Pin(i, Pin.OUT) for i in range(11,-1,-1)]

for i in range(11,-1,-1):
    leds[i].value(1)

print([leds[i].value() for i in range(11,-1,-1)])
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]

leds[9].value(1)
print([leds[i].value() for i in range(12)])
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
# 9th pin never to be activated, neither 10th nor 11th.

while True:
    val = int(input('input 0~11 : '))
    try:
        if leds[val].value():
            leds[val].value(0)
        else:
            leds[val].value(1)
        print([leds[i].value() for i in range(12)])
    except (ValueError, IndexError):
        pass
