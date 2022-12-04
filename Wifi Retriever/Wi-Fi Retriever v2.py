###############################################################
#                   Written in Python 3.11.0                  #
#                                                             #
#                Copyright © 2022 Jelmar Orapa                #
###############################################################

from tkinter import *
from tkinter.ttk import *
import tkinter
import subprocess
import re
import tkinter.messagebox

root = tkinter.Tk()
root.title("Wi-Fi Retriever By Jelmar Orapa")
root.geometry("500x245")
root.configure(bg='#F4F4F4')

# set colours
bg_colour = "#3d6466"

#Popup message
def onstart():
    tkinter.messagebox.showinfo("Welcome to Wi-Fi Retriever!",  "Please use with permission!")  

#subprocess to get wifi passwords using netsh in cmd
#credits to David Bombal for the most part of this section, i learned from his youtube channel
#I only edited a few from his original code to make it to work as i intended
    
def getwifi():

        command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True, shell=True).stdout.decode()

        profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

        wifi_list = []

        if len(profile_names) != 0:
            for name in profile_names:
                wifi_profile = {}
                profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True, shell=True).stdout.decode()
                if re.search("Security key           : Absent", profile_info):
                    continue
                else:
                    wifi_profile[ "Wi-Fi Name is" ] = name
                    profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True, shell=True).stdout.decode()

                    password = re.search("Key Content            : (.*)\r", profile_info_pass)
                    if password == None:
                        wifi_profile[ "Password is" ] = None
                    else:
                        wifi_profile[ "Password is" ] = password[1]
                    wifi_list.append(wifi_profile) 

        for x in range(len(wifi_list)):
            import sys
            file = open('Wi-Fi.txt', 'a')
            sys.stdout = file
            print(wifi_list[x])
            file.close()

#Print Youtube Channel
def mychannel():
        import sys
        file = open('Wi-Fi.txt', 'a')
        sys.stdout = file
        print("\n Thank you for using this simple program! \n Please support my Youtube Channel... \n https://www.youtube.com/@thetechinquirer5477 \n Copyright © 2022 Jelmar Orapa \n")
        file.close()

#function to print subprocess on gui screen
def readwifi():
        f = open("Wi-Fi.txt", "r")
        wipass = f.read()

        my_text.insert(END, wipass)
        f.close()

#creating a textbox for the subprocess output
my_text = Text(root, width=70, height=11, font=("Arial", 10))
my_text.pack(pady=10, padx=10)

#creating a button
readbutton = tkinter.Button(root, text="Retrieve Wi-Fi Passwords!", bg=bg_colour, fg="white", font='Arial 12 bold', command= lambda:[getwifi(), mychannel(), readwifi()])
readbutton.config(width=23, height=1, bg=bg_colour)
readbutton.pack()

#Centering on screen
root.eval('tk::PlaceWindow . center')

#Starting popup message
onstart()

#starting the application
root.mainloop()

###############################################################
#                   Written in Python 3.11.0                  #
#                                                             #
#                Copyright © 2022 Jelmar Orapa                #
###############################################################
