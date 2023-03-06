import time
from tkinter import *
from tkinter import messagebox
 
 

root = Tk()
root.geometry("400x300")
root.title("Countdown timer")
root.config(bg='pink')
  

hour=StringVar()
minute=StringVar()
second=StringVar()
  

hour.set("00")
minute.set("00")
second.set("00")
  

hour_box= Entry(root, width=3, font=("Arial",18,""),textvariable=hour)
hour_box.place(x=80,y=20)
  
mins_box = Entry(root, width=3, font=("Arial",18,""),textvariable=minute)
mins_box.place(x=130,y=20)
  
sec_box = Entry(root, width=3, font=("Arial",18,""),textvariable=second)
sec_box.place(x=180,y=20)
  
  
def countdowntimer():
    try:
        # store the user input
        user_input = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        messagebox.showwarning('', 'Invalid Input!')
    while user_input >-1:
         
        # divmod(firstvalue = user_input//60, secondvalue = user_input%60)
        mins,secs = divmod(user_input,60)
  
        # Converting the input entered in mins or secs to hours,
        hours=0
        if mins >60:

            hours, mins = divmod(mins, 60)
         
        # store the value up to two decimal places
        # using the format() method
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
  
        # updating the GUI window 
        root.update()
        time.sleep(1)
  
        # if user_input value = 0, then a messagebox pop's up
        # with a message
        if (user_input == 0):
            messagebox.showinfo("START", "TIME UP")
       
        user_input -= 1
 
# button widget
btn = Button(root, text='START', bd='5',command= countdowntimer)
btn.place(x = 80,y = 120)
  
root.mainloop()
Output
