from tkinter import *
import tkinter as Tkinter


def callback():
    parent_widget = Tkinter.Tk()
    canvas_widget = Tkinter.Canvas(parent_widget, bg="blue", width=1920, height=1080)
    canvas_widget.pack()
    Tkinter.mainloop()

parent_widget = Tkinter.Tk()
button_widget = Tkinter.Button(parent_widget, text="Open Canvas", command=callback)
button_widget.pack()
Tkinter.mainloop()