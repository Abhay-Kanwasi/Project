from tkinter import *
import speedtest

speed = Tk()
speed.title(" Internet Speed Test ")
speed.geometry("500x500")
speed.config(bg = "#FFFDD0")

lab = Label(speed,text=" Speed Tester ", font = ("Calibri",20,"bold"),bg="#FFFDD0",fg="Black")
lab.place(x=150,y=30,height=35,width=200)

lab = Label(speed,text=" Download Speed ", font = ("Calibri",18,"bold"),bg="#52595D",fg="Black")
lab.place(x=150,y=90,height=35,width=200)

lab = Label(speed,text="00", font = ("Calibri",20,"bold"),bg="#52595D",fg="Black")
lab.place(x=150,y=140,height=35,width=200)

lab = Label(speed,text=" Upload Speed ", font = ("Calibri",20,"bold"),bg="#52595D",fg="Black")
lab.place(x=150,y=210,height=35,width=200)

lab = Label(speed,text="00", font = ("Calibri",20,"bold"),bg="#52595D",fg="Black")
lab.place(x=150,y=260,height=35,width=200)

button = Button(speed,text="CHECK SPEED",font = ("Time New Roman",20,"bold"),relief=RAISED,bg="Green")
button.place(x=137,y=360,height=35,width=230) 

speed.mainloop()