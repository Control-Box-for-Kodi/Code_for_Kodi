#!/usr/bin/env python3
from tkinter import *
import tkinter as tk

from tkinter.font import Font
from tkinter import messagebox
import time
import random
import gaugelib
import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)

win = tk.Tk()
a5 = PhotoImage(file="g1.png")
win.tk.call('wm', 'iconphoto', win._w, a5)
win.title("Energy Produced by Bikes (Watts)")
win.geometry("200x200+0+0")
win.resizable(width=True, height=True)
win.configure(bg='black')
g_value=0
x=0

def read_every_second():
    if(ser.in_waiting >0):
        line = ser.readline()
        p1.set_value(int(line))

    win.after(100, read_every_second)

p1 = gaugelib.DrawGauge2(
    win,
    max_value=100.0,
    min_value=0.0,
    size=200,
    bg_col='black',
    unit = "Energy (W)",bg_sel = 2)
p1.pack(side=LEFT)



read_every_second()
mainloop()
