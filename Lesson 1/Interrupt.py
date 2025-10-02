import machine, utime, urandom

LED = machine.Pin(15, machine.Pin.OUT)
BTN = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

DEBOUNCE = 50
DBL_WIN  = 500

def wait_press():

    while BTN.value(): pass
    while not BTN.value(): pass
    utime.sleep_ms(DEBOUNCE)
    while BTN.value(): pass

def double_click():
    wait_press()
    t0 = utime.ticks_ms()
    while utime.ticks_diff(utime.ticks_ms(), t0) < DBL_WIN:
        if BTN.value():
            wait_press()
            return True
    return False

while True:
    LED.value(0)
    utime.sleep_ms(5000 + (urandom.getrandbits(12) % 5001))  # 5–10 s
    LED.value(1)
    t0 = utime.ticks_ms()
    wait_press()
    rt = utime.ticks_diff(utime.ticks_ms(), t0)
    LED.value(0)
    print("Reaction:", rt, "ms")
    print("Double-click to retry")
    if double_click():
        print("Restart\n")
    else:
        print("No restart\n")
