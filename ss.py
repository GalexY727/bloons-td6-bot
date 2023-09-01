import pyautogui

im1 = pyautogui.screenshot(region=(150,1000,1200,80))#region=(150,800,1200,280))
im1.save(r"./region.png")