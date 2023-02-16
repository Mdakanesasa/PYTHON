from tkinter import*

any_ =Tk()

any_.title('sasa')



             
label=Label(any_,text="USERNAME")
label.grid(column=1,row=2)

label2=Label(any_,text="ENTER PASSWORD")
label2.grid(column=1,row=3)

ent=Entry(any_,bg="grey")
ent.grid(column=2,row=2)


ent=Entry(any_,bg="grey")
ent.grid(column=2,row=3)


play_=PhotoImage(file=r"C:\Users\AFTERNOON SESSION SD\Desktop\python\images\login-icon-shiny-glossy-internet-button-on-grey-background-FPMGJG.png")
label=Label(image=play_)
photoimage = play_.subsample(3, 3)
play_btn=Button(any_,image=play_)
play_btn.grid(column=2,row=4)





























any_.mainloop()






