
import pyautogui
import time
 
def click(): 
    pyautogui.click()
 
def main():
    while True:
        time.sleep(0.1)     
        click()

 
main()