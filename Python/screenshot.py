import pyautogui
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 200, height = 160)
canvas1.pack()

def takeScreenshot ():
 myScreenshot = pyautogui.screenshot()
 save_path = filedialog.asksaveasfilename(defaultextension='.png')
 myScreenshot.save(save_path+"")

myButton = tk.Button(text='Take Screenshot', command=takeScreenshot, bg='green',fg='white',font= 10)
canvas1.create_window(100, 80, window=myButton)

root.mainloop()