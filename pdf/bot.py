import pyautogui
import time

time.sleep(4)

arq = open("texto.txt", "r", encoding="utf-8")

for palavra in arq:
    pyautogui.typewrite(palavra)
    pyautogui.press("enter")
