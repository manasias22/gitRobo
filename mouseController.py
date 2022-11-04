
import pyautogui
import time
 
def click(): 
    time.sleep(0.1)     
    pyautogui.click()
 
def main():
    time.sleep(10)
    while True:
        click()
 
main()