from machine import Pin, PWM, ADC
import time
import os, sys, math

"""
https://fishandwhistle.net/post/2016/raspberry-pi-pure-python-infrared-remote-control/
"""

pin = 26
sensor = ADC(Pin(pin))


def binary_aquire(pin, duration):
    def _is_less_than_byte(results):
        return len(results) < 2500

    # print('duration : {}'.format(duration))

    t0 = time.time()
    results = []

    while (time.time() - t0) < duration and _is_less_than_byte(results):
        val = sensor.read_u16()
        # print(val)
        results.append(val)
    return results


def on_ir_receive(pinNo, bouncetime=150):
    # when edge detect is called (which requires less CPU than constant
    # data acquisition), we acquire data as quickly as possible
    data = binary_aquire(pinNo, bouncetime / 1000.0)
    if len(data) < bouncetime:
        return False

    rate = len(data) / (bouncetime / 1000.0)
    pulses = []
    i_break = 0
    # detect run lengths using the acquisition rate to turn the times in to microseconds
    for i in range(1, len(data)):
        if (data[i] != data[i - 1]) or (i == len(data) - 1):
            pulses.append((data[i - 1], int((i - i_break) / rate * 1e6)))
            i_break = i
    # decode ( < 1 ms "1" pulse is a 1, > 1 ms "1" pulse is a 1, longer than 2 ms pulse is something else)
    # does not decode channel, which may be a piece of the information after the long 1 pulse in the middle
    outbin = ""
    # p = [print(el) if int(el[0]) < 60000 else "" for el in pulses]
    # sys.exit()
    for val, us in pulses:
        if val > 60000:
            continue

        if outbin and us > 2000:
            break
        elif us < 1000:
            outbin += "0"
        elif 1000 < us < 2000:
            outbin += "1"
    try:
        return int(outbin, 2)
    except ValueError:
        # probably an empty code
        return None


if __name__ == "__main__":
    ex_data = sensor.read_u16()
    current_data = sensor.read_u16()
    try:
        print("Starting IR Listener")
        while True:
            # print("Waiting for signal")

            while abs(current_data - ex_data) < 60000:
                ex_data = current_data
                current_data = sensor.read_u16()

            code = on_ir_receive(pin)
            if code:
                print(str(hex(code)))
            elif code == False:
                print("Invalid code : False")
            elif code == None:
                print("Invalid code : None")
            else:
                print("Invalid code : else")

            ex_data = current_data
            current_data = sensor.read_u16()

    except KeyboardInterrupt:
        pass
    except RuntimeError:
        # this gets thrown when control C gets pressed
        # because wait_for_edge doesn't properly pass this on
        pass
    print("Quitting")
