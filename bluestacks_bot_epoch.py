### window focused bot for bluestacks ###
from bluestacks_bot_timing import *
import pyautogui
import random
import time
import math

# todo: factor out hardcoded strings
# input from gui?
def RunBot(time_in_min):
    stop = False
    runtime = time.time() + time_in_min*60

    # tele -> atk x2
    # random intervals to prevent pattern recog
    while (not stop):
        pyautogui.press("c")
        pyautogui.press("space", presses=random.randint(1,3), interval=0.3)
        time.sleep(0.75)
        stop = time.time() > runtime
        print(math.floor((runtime - time.time())/60), "minutes left")


