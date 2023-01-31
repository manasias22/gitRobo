import os
import pyautogui
 
# prompts message on screen and takes the
# input command in val variable
val = pyautogui.prompt("Enter Shell Command")
 
# executes the value of val variable
os.system(val)