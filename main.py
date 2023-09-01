from pyautogui import *
import pyautogui
import keyboard
import time

print("Starting!")

x = 0

while 1:
    if x == 0:
        image = 'heli.png'
    elif x == 1:
        image = 'snipercrate.png'
    elif x == 2:
        image = 'jungledruid.png'

    leftTabOpen = pyautogui.locateOnScreen('dropdown.png', region=(150,800,1250,280), confidence=0.9)
    result = pyautogui.locateOnScreen(image, region=(150,800,1250,280), confidence=0.9)

    if result != None:
        result = pyautogui.center(result)
        x, y = result
        # get how many pixels it is from the left.
        if (leftTabOpen != None):
            x = x - 400
        x = x/120
        x = int(x)
        if x == 11:
            x = 'minus'
        elif x == 12:
            x = 'plus'
        # press the key corresponding to x
        keyboard.press_and_release(str(x))
    
    time.sleep(1)
    x = (x + 1) % 3
