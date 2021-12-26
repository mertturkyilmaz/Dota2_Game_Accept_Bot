##OYUN KABUL ET
import pyautogui
from pyautogui import *
from time import sleep

    
def check_screen():
    buttonSeeker = pyautogui.locateCenterOnScreen("fila.png", minSearchTime=2000)
            
    if buttonSeeker != None:
        #print(f'Found {button_pos}')
        pyautogui.moveTo(buttonSeeker)
        pyautogui.click(buttonSeeker)  
        return True
    
    return False

def main():
    queue_counter = 0

    print('Oyun Aranıyor..', end="\n\n")
    
    while True:
        if check_screen():
            queue_counter += 1
            print(f'Hadi GL & HF: {queue_counter}')
            
            sleep(6)
            break


main()            
