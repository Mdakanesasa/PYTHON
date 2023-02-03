from tkinter import*

window=Tk()
window.title("calculator")
ent =Entry(window,width=30,borderwidth=5)
ent.grid(column=0,row=0,columnspan=3,pady=10,padx=10)


def btn_equals():
    try:
        current = ent.get()
        total = eval(current)
        ent.delete(0, END)
        ent.insert(0, str(total))
    except:
        ent.delete(0, END)
        ent.insert(0, "error")

def btn_press(clear):
    current=ent.get()
    ent.delete(0,END)

    

def btn_click(number):
    current=ent.get()
    ent.delete(0,END)
    ent.insert(0,str(current)+str(number))
    

    


but_click7=Button(window,text="7",bg="pink",padx=30, pady=15,command=lambda:btn_click(7))
but_click7.grid(column=0,row=1)

but_click4=Button(window,text="4",bg="pink",padx=30, pady=15,command=lambda:btn_click(4))
but_click4.grid(column=0,row=2)

but_click1=Button(window,text="1",bg="pink",padx=30, pady=15,command=lambda:btn_click(1))
but_click1.grid(column=0,row=3)


but_click8=Button(window,text="8",bg="aqua",padx=30, pady=15,command=lambda:btn_click(8))
but_click8.grid(column=1,row=1)

but_click5=Button(window,text="5",bg="aqua",padx=30, pady=15,command=lambda:btn_click(5))
but_click5.grid(column=1,row=2)

but_click2=Button(window,text="2",bg="aqua",padx=30, pady=15,command=lambda:btn_click(2))
but_click2.grid(column=1,row=3)



but_click9=Button(window,text="9",bg="purple",padx=30, pady=15,command=lambda:btn_click(9))
but_click9.grid(column=2,row=1)

but_click6=Button(window,text="6",bg="purple",padx=30, pady=15,command=lambda:btn_click(6))
but_click6.grid(column=2,row=2)

but_click3=Button(window,text="3",bg="purple",padx=30, pady=15,command=lambda:btn_click(3))
but_click3.grid(column=2,row=3)


clear=Button(window,text="AC",bg="white",padx=30, pady=15,command=lambda:btn_press(""))
clear.grid(column=3,row=1)

but_click0=Button(window,text="0",bg="white",padx=30, pady=20,command=lambda:btn_click(0))
but_click0.grid(column=0,row=4)

but_clickadd=Button(window,text="+",bg="green",padx=35, pady=15,command=lambda:btn_click("+"))
but_clickadd.grid(column=3,row=3)

but_clicksub=Button(window,text="-",bg="green",padx=35, pady=20,command=lambda:btn_click("-"))
but_clicksub.grid(column=3,row=4)

but_clickmult=Button(window,text="x",bg="green",padx=30, pady=20,command=lambda:btn_click("*"))
but_clickmult.grid(column=2,row=4)

divide=Button(window,text="/",bg="green",padx=30, pady=20,command=lambda:btn_click("/"))
divide.grid(column=1,row=4)

equal=Button(window,text="=",bg="green",padx=35, pady=15,command=lambda:btn_equals())
equal.grid(column=3,row=2)


window.mainloop()
