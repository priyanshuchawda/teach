# If not already installed, install pyautogui using: pip install pyautogui

import pyautogui

pyautogui.moveTo(1000, 1000, duration=2)
pyautogui.click()
pyautogui.typewrite('Hello, Python!', interval=0.2)
