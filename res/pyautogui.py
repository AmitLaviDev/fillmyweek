import pyautogui
from pynput.keyboard import Controller
from time import sleep

keyboard = Controller()


def okta_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y)


def input_text(text):
    for char in text:
        keyboard.type(char)
        sleep(0.05)


def password_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click(x, y)
