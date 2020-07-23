import pyperclip
import pyautogui
import time

#Gives time to get to application
time.sleep(5)

#Words to be copied
lyrics = "Insert Lyrics/Script here"

#Splits long text into words
split = lyrics.split()

#loops pressing buttons
for x in range(0,len(split)):
    pyperclip.copy(split[x])
    pyautogui.keyDown('command')
    pyautogui.keyDown('v')
    pyautogui.keyUp('command')
    pyautogui.keyUp('v')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(0.1)