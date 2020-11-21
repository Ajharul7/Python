from PIL import ImageGrab
import keyboard
from tkinter import filedialog
while True:
    try:
        if keyboard.is_pressed('`'):
           image = ImageGrab.grab()
           save_path = filedialog.asksaveasfilename(defaultextension='.png')
           image.save(save_path+"")
           break
        else:
            pass
    except:
        break