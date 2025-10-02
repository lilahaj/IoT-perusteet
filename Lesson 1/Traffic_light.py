import machine
import utime

# LED-pinnit
led_red    = machine.Pin(15, machine.Pin.OUT)
led_yellow = machine.Pin(14, machine.Pin.OUT)
led_green  = machine.Pin(13, machine.Pin.OUT)

# Jalankulkijan nappi (PULL_DOWN → 1 = painettu)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

REQUEST_DELAY      = 5    # viive napista vihreään siirtymisen aloitukseen
RED_YELLOW_TIME    = 1    # punainen + keltainen yhtä aikaa
GREEN_TIME         = 5    # vihreä auki aika
YELLOW_TIME        = 2    # keltainen ennen punaista
DEBOUNCE_MS        = 200  # napin debouncaus

def set_lights(r=False, y=False, g=False):
    led_red.value(1 if r else 0)
    led_yellow.value(1 if y else 0)
    led_green.value(1 if g else 0)

def run_cycle():
    set_lights(r=True, y=False, g=False)

    for _ in range(REQUEST_DELAY):
        utime.sleep(1)

    # Punainen + keltainen hetken (eurooppalainen vaihe)
    set_lights(r=True, y=True, g=False)
    utime.sleep(RED_YELLOW_TIME)

    set_lights(r=False, y=False, g=True)
    utime.sleep(GREEN_TIME)

    set_lights(r=False, y=True, g=False)
    utime.sleep(YELLOW_TIME)

    set_lights(r=True, y=False, g=False)

# Alkutila: punainen palaa jatkuvasti
set_lights(r=True, y=False, g=False)

cycle_running = False
last_press_ms = 0

while True:
    now = utime.ticks_ms()
    if button.value() == 1 and not cycle_running and utime.ticks_diff(now, last_press_ms) > DEBOUNCE_MS:
        last_press_ms = now
        cycle_running = True
        run_cycle()
        cycle_running = False

    if not cycle_running:
        led_red.value(1)
        led_yellow.value(0)
        led_green.value(0)

    utime.sleep_ms(10)
