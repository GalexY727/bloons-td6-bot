from pyautogui import *
import pyautogui
import keyboard
import time

print("Starting!")

index = 0

while 1:
    if index == 0:
        image = './media/heli.png'
    elif index == 1:
        image = './media/snipercrate.png'
    elif index == 2:
        image = './media/jungledruid.png'
    elif index == 3:
        image = './media/monkeynomics.png'

    leftTabOpen = pyautogui.locateOnScreen('./media/dropdown.png', region=(150,800,1250,280), confidence=0.9)
    result = pyautogui.locateOnScreen(image, region=(150,800,1250,280), confidence=0.9)

    if result != None:
        result = pyautogui.center(result)
        x, y = result
        # get how many pixels it is from the left.
        if (leftTabOpen != None):
            x = x - 400
        x = (x-160)/90
        x = int(x+0.5)

        if x == 10:
            x = '0'
        elif x == 11:
            x = '-'
        elif x == 12:
            x = '+'
        # press the key corresponding to x
        keyboard.press_and_release(str(x))
    
    time.sleep(1)
    index = (index + 1) % 4
