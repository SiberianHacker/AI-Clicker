import cv2
import pyautogui
import numpy as np
import os
import keyboard

object_files = [f for f in os.listdir("objects") if f.endswith('.png')]
objects = [cv2.imread(os.path.join("objects", f), cv2.IMREAD_UNCHANGED) for f in object_files]
running = True

def stop_program():
    global running
    running = False

keyboard.add_hotkey('F6', stop_program)

while running:
    screen = pyautogui.screenshot()
    screen_np = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    for obj, obj_file in zip(objects, object_files):
        res = cv2.matchTemplate(screen_np, obj, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)
        for pt in zip(*loc[::-1]):
            x, y = pt[0] + obj.shape[1] // 2, pt[1] + obj.shape[0] // 2
            pyautogui.click(x, y)