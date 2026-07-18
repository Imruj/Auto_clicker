import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

clicking = False
START_STOP = KeyCode(char='j')
END = KeyCode(char='k')
mouse = Controller()

def cycle():
    while True:
        if clicking:
            print("clicked", flush=True)
            mouse.click(Button.left,1)
            time.sleep(1)
        else:
            time.sleep(0.1)

def clicker(key):
    if (key == START_STOP):
        global clicking
        clicking = not clicking
    if (key == END):
        return False
    
click_thread = threading.Thread(target=cycle)
click_thread.start()

with Listener(on_press=clicker) as listener:
    listener.join()