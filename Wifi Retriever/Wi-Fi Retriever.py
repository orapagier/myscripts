from tkinter import *
import tkinter
import subprocess
import re
import os

root = tkinter.Tk()
root.title("Wi-Fi Retriever")
root.geometry("500x255")

def submitFunction():

    os.system("getwifi.exe")

def readwifi():
        f = open("Wi-Fi.txt", "r")
        wipass = f.read()

        my_text.insert(END, wipass)
        f.close()

my_text = Text(root, width=60, height=10, font=("Arial", 12))
my_text.pack(pady=10, padx=10)

readbutton = tkinter.Button(root, text="Show Wi-Fi Passwords!", command=readwifi)
readbutton.config(width=20, height=2)

submitFunction()
 
readbutton.pack()
root.mainloop()
