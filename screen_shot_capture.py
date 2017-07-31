from subprocess import call
import time
from time import gmtime, strftime

def take_screen_shot():
    # save screen shots where
    call(["screencapture", "Screenshot" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ".jpg"])

def build_screen_shot_base():
    # give users time to start the process
    time.sleep(10)

    while True:
        take_screen_shot()
        time.sleep(10)


build_screen_shot_base()
    

