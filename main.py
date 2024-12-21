import pyautogui
from config import *
import time
import b64coder

def lock():
    pyautogui.hotkey('win','r')
    time.sleep(1)
    pyautogui.typewrite('rundll32.exe user32.dll, LockWorkStation\n')

def move_tile_cursor(x: int,y: int):
    for _ in range(abs(x)):
        if (x > 0):
            pyautogui.press('right')
        else:
            pyautogui.press('left')
    for _ in range(y):
        if (y > 0):
            pyautogui.press('down')
        else:
            pyautogui.press('up')


time.sleep(3)

new_img_lines = IMAGE[1:][:-1].split('\n')

X_DIR = 1

X_OFFSET = 0
Y_OFFSET = 0

CUR_X = 0
CUR_Y = 0

for l in new_img_lines:
    tl = None
    if (X_DIR == -1):
        tl = l[::-1]
    else:
        tl = l
    for i in tl:
        color_index = b64coder.FromBase64(i)

        next_tile = (CENTER_TILE[0] + (TILE_SIZE[0] * X_DIR),CENTER_TILE[1])
        
        if (color_index != 5 or X_OFFSET >= MAX_X_OFFSET or Y_OFFSET >= MAX_Y_OFFSET):
            #pyautogui.moveTo(next_tile[0] + (X_OFFSET * TILE_SIZE[0]),next_tile[1] + (Y_OFFSET * TILE_SIZE[1]),0.0)
            move_tile_cursor(X_OFFSET + X_DIR,Y_OFFSET)
            #pyautogui.leftClick()

            #pyautogui.moveTo(PICK_TILE_BUTTON[0],PICK_TILE_BUTTON[1],0.0)
            #pyautogui.leftClick()

            '''COLOR_BUTTON = ((color_index * COLOR_BUTTON_WIDTH) + COLOR_BUTTON_START_X,COLOR_BUTTON_Y)
            pyautogui.moveTo(COLOR_BUTTON[0],COLOR_BUTTON[1],0.2)'''
            pyautogui.press(COLOR_KEYS[color_index],2,0.02)
            time.sleep(0.03)
            pyautogui.press(COLOR_KEYS[color_index],2,0.02)
            time.sleep(0.03)
            pyautogui.press(COLOR_KEYS[color_index],2,0.02)

            #pyautogui.leftClick()
            pyautogui.press('enter')

            X_OFFSET = 0
            Y_OFFSET = 0
        else:
            X_OFFSET += X_DIR
    
    '''next_tile = (CENTER_TILE[0] + (TILE_SIZE[0] * X_DIR),CENTER_TILE[1] + TILE_SIZE[1])
    pyautogui.moveTo(next_tile[0],next_tile[1],0.0)
    pyautogui.leftClick()'''
    move_tile_cursor(X_DIR,1)
    X_DIR *= -1
#lock()