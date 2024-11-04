import pyautogui
from time import sleep


def okta_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y)


def input_text(text):
    for char in text:
        if char.isupper():
            # Press Shift + character for uppercase letters
            pyautogui.keyDown("shift")
            pyautogui.press(char.lower())
            pyautogui.keyUp("shift")
        else:
            pyautogui.press(char)
        sleep(0.05)


def password_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y)
