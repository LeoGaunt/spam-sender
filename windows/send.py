import pyperclip
import pyautogui
import time

Time = int(input("How long do you need to reach your appllication where you want the messages? (In seconds): "))
wait = int(input("How long would you like between each message? (In seconds): "))

#Gives time to get to application
time.sleep(Time)

#Words to be copied
lyrics = "Insert Lyrics/Script here"

#Splits long text into words
split = lyrics.split()

#loops pressing buttons
for x in range(0,len(split)):
    pyperclip.copy(split[x])
    pyautogui.keyDown('control')
    pyautogui.keyDown('v')
    pyautogui.keyUp('control')
    pyautogui.keyUp('v')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(wait)