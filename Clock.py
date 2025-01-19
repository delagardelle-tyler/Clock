"""
Title: Clock
Author: Tyler Delagardelle
Description: A simple clock app.
"""

from tkinter import Tk
from tkinter import Label
import time
import sys
#opens base window
window = Tk()
window.title("Digital clock")
#clock title
clock = Label(window , font = ("calibri" , 90) , bg = "#966659" , fg = "white")
clock.pack()

def updateClock():
    #collects current time
    timeVar = time.strftime("%I:%M:%S %p")
    #changes text to current time
    clock.config(text=timeVar)
    #after 1 seconds, update clock
    clock.after(1000,updateClock)

updateClock()

window.mainloop()

