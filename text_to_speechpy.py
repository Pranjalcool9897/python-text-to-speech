from tkinter import *
import pyttsx3

eng=pyttsx3.init()
eng.setProperty('rate',150)

root=Tk()
root.geometry("500x600")

def talk():
    eng.say(ent.get())

    eng.runAndWait()
    ent.delete(0,END)


ent=Entry(root,font=("arial",20))
ent.pack(pady=20)
but=Button(root,text="Say it!",fg="blue",command=talk)
but.pack()







root.mainloop()