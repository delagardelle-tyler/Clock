"""
Title: Clock
Author: Tyler Delagardelle
Description: A simple clock app.
"""

from tkinter import Tk
from tkinter import Label
import time
import sys

window = Tk()
window.title("Digital clock")

clock = Label(window , font = ("calibri" , 90) , bg = "#966659" , fg = "white")
clock.pack()

def updateClock():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(1000,updateClock)

updateClock()

window.mainloop()

