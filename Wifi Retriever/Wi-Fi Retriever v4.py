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
import sys
import tkinter.messagebox
import datetime

root = tkinter.Tk()
root.title("Wi-Fi Retriever By Jelmar Orapa")
root.geometry("514x300")
root.configure(bg='#F4F4F4')

# set colours
bg_colour = "#3d6466"
    
#Popup message
def onstart():
    tkinter.messagebox.showinfo("Welcome to Wi-Fi Retriever!",  "Please use with permission!")  

#subprocess to get wifi passwords using netsh in cmd
def getwifi():
    wifiList = []

    # getting meta data
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], shell=True)

    # # decoding meta data
    data = meta_data.decode('utf-8', errors="backslashreplace")

    # # spliting data line by line
    data = data.split('\n')

    # creating a list of profiles
    profiles = []

    # traverse the data
    for i in data:

        # find "All User Profile" in each item
        if "All User Profile" in i:

            # if found
            # split the item
            i = i.split(":")

            # item at index 1 will be the wifi name
            i = i[1]

            # formatting the name
            # first and last chracter is use less
            i = i[1:-1]

            # appending the wifi name in the list
            profiles.append(i)

    # printing heading
    file = open('wifi.txt', 'a')
    sys.stdout = file
    print("-----------------------------------------------------------")
    print("{:<30}--->{:<}".format("Wi-Fi Name", " Password"))
    print("-----------------------------------------------------------")
    file.close()

    # traversing the profiles
    for i in profiles:

        # try catch block begins
        # try block
        try:
            # getting meta data with password using wifi name
            results = subprocess.check_output(['netsh', 'wlan', 'show',
                                              'profile', i, 'key=clear'], shell=True)

            # decoding and splitting data line by line
            results = results.decode('utf-8', errors="backslashreplace")
            results = results.split('\n')

            # finding password from the result list
            results = [b.split(":")[1][1:-1]
                       for b in results if "Key Content" in b]

            # if there is password it will print the password
            try:


                #my_textbox.insert(END, ("{:<30}---> {:<}".format(i, results[0])))
                file = open('wifi.txt', 'a')
                sys.stdout = file
                print("{:<30}---> {:<}".format(i, results[0]))
                #print(i)
                #print(results[0])
                wifiList.append((i, results[0]))
                file.close()

                
            # else it will print blank in front of password
            except IndexError:


                file = open('wifi.txt', 'a')
                sys.stdout = file
                print("{:<30}---> {:<}".format(i, ""))
                #print(i)
                wifiList.append((i, ""))
                file.close()

                
        # called when this process get failed
        except subprocess.CalledProcessError:
            file = open('wifi.txt', 'a')
            sys.stdout = file
            print("Subprocess Error Occured")
            file.close()
    return wifiList

#Print Youtube Channel
def myYTchannel():
        import sys
        file = open('wifi.txt', 'a') 
        sys.stdout = file
        print("\nThank you for using this simple program! \nPlease support my Youtube Channel... \nhttps://www.youtube.com/@thetechinquirer5477 \nCopyright © 2022 Jelmar Orapa \n")
        now = datetime.datetime.now()
        print("Retrieved Date:", now)
        print("\n----------------Wi-Fi Password Retriever v4---------------- \n")
        file.close() 

#function to print subprocess on gui screen
def readwifi():
        f = open("wifi.txt", "r")
        wipass = f.read()
        text.insert(END, wipass)
        f.close()

# Group1 Frame ----------------------------------------------------
group1 = tkinter.LabelFrame(root, text="Wi-Fi Retriever v4", padx=5, pady=5)
group1.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=tkinter.E+tkinter.W+tkinter.N+tkinter.S)

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

group1.rowconfigure(0, weight=1)
group1.columnconfigure((0,1), weight=1)

text = tkinter.Text(group1)
text.pack()

btn_Image = tkinter.Button(root, text='Retrieve Wi-Fi Passwords',
                           bg='gray', fg='white', font='Arial 10 bold',
                           command= lambda:[getwifi(), myYTchannel(), readwifi()])
btn_Image.grid(row=2, column=0, padx=(10), pady=10, sticky=tkinter.S)
btn_Image.config(width=23, height=1, bg=bg_colour)

#Centering on screen
root.eval('tk::PlaceWindow . center')

#Starting popup message
onstart()
#getwifi()
#readwifi()

#starting the application
root.mainloop()

###############################################################
#                   Written in Python 3.11.0                  #
#                                                             #
#                Copyright © 2022 Jelmar Orapa                #
###############################################################
