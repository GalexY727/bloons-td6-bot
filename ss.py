import pyautogui

im1 = pyautogui.screenshot(region=(1272,1031,30,30))#region=(150,800,1200,280))
im1.save(r"./region.png")