import sys #to import system files
from tkinter import *   #whole module is imported
import time #importing local time

#Used to display time on the label
def DigitalClock():
    current_time= time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(100,DigitalClock)

#making window
window=Tk()
window.title('Digital Clock') #adding title to the window


#giving name to our digital clock and styling it
message= Label(window,text="Digital Clock", fg="grey")
message.grid(row=0,column=0)

clock= Label(window, font=("times",150,"bold"),fg="grey")
clock.grid(row=1,column=0)
DigitalClock()
mainloop() #loop is closed
