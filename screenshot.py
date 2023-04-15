from PIL import ImageGrab
import pyautogui
import time
import subprocess
import os

"""
img = ImageGrab.grab(bbox=(0, 0, 300, 300))
img.save("screenshot1.png")

with pyautogui.hold("alt"):
    pyautogui.press("tab")
    
time.sleep(1)

img = ImageGrab.grab(bbox=(0, 0, 1000, 1000))
img.save("screenshot2.png")

print(pyautogui.position())

pyautogui.moveTo(3352, 95)
pyautogui.click()
pyautogui.alert('This is the message to display.')"""

pages_to_shot = 100
page_count_start = 301
subfolder = "pages"


# first, alt tab to open firefox
pyautogui.hotkey('alt', 'tab')
# move the mouse to next page position
pyautogui.moveTo(1557, 604)
# sleep so alt tab works
time.sleep(1)

for page in range(page_count_start, page_count_start + pages_to_shot):

    # notify which screenshot I'm taking
    # subprocess.Popen(['notify-send', f"{page}/{pages_to_shot}"])

    # grab and save screenshot
    img = ImageGrab.grab(bbox=(404, 194, 1508, 1021))
    img.save(os.path.join(subfolder, f"stranka_{page:04d}.png"))
    
    # move to next page
    pyautogui.click()
    # sleep for next page to render
    time.sleep(3)
    

subprocess.Popen(['notify-send', f"Done!"])


