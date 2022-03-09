import random, time
from threading import Lock

global button_a
global button_b

button_a = None
button_b = None

l_b = Lock()
l_a = Lock()

def setup_sensors():
    print("All sensors have been set up successfully!")
    return True

def setup_buttons():
    print("All buttons have been set up successfully!")
    return True

def setup_display():
    print("The display has been set up successfully!")
    return True

def read_light_level():
    return random.randint(50,70)

def read_temp():
    return random.randint(50,70)

def read_battery():
    return 95

def wait_for_button_a():
    global button_a
    with l_a:
        if not button_a:
            button_a = time.time() + random.randint(30, 100)
    while time.time() <= button_a:
        time.sleep(0.1)
    with l_a:
        if time.time() >= button_a:
            button_a = None
    return

def wait_for_button_b():
    global button_b
    with l_b:
        if not button_b:
            button_b = time.time() + random.randint(30, 100)
    while time.time() <= button_b:
        time.sleep(0.1)
    with l_b:
        if time.time() >= button_b:
            button_b = None
    return

def clear_display():
    print("           ----------------")

def write_line_to_display(text):
    if len(text) > 16:
        raise Exception("Display width is 16 characters")
    print("DISPLAY:   ", end='')
    for t in text:
        print(t, end='')
    print("")

