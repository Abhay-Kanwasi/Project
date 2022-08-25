from tkinter import *
import speedtest

def speedcheck():
    speed = speedtest.Speedtest()
    speed.get_servers()
    download_speed = str(round(speed.download()/(10**6),3))+ "Mbps" # sp.download() :- This function give us speed in bit per second. then we convert it by dividing 10**6.
    upload_speed = str(round(speed.upload()/(10**6),3)) + "Mbps"
    lab_download.config(text =download_speed)
    lab_upload.config(text=upload_speed)
     
speed = Tk()
speed.title(" Internet Speed Test ")
speed.geometry("500x500")
speed.config(bg = "#FFFDD0")

lab = Label(speed,text=" Speed Tester ", font = ("Calibri",20,"bold"),bg="#FFFDD0",fg="Black")
lab.place(x=150,y=30,height=35,width=200)

lab = Label(speed,text=" Download Speed ", font = ("Calibri",18,"bold"),bg="#52595D",fg="Black")
lab.place(x=150,y=90,height=35,width=200)

lab_download = Label(speed,text="00", font = ("Calibri",20,"bold"),bg="#52595D",fg="Black")
lab_download.place(x=150,y=140,height=35,width=200)

lab = Label(speed,text=" Upload Speed ", font = ("Calibri",20,"bold"),bg="#52595D",fg="Black")
lab.place(x=150,y=210,height=35,width=200)

lab_upload = Label(speed,text="00", font = ("Calibri",20,"bold"),bg="#52595D",fg="Black")
lab_upload.place(x=150,y=260,height=35,width=200)

button = Button(speed,text="CHECK SPEED",font = ("Time New Roman",20,"bold"),relief=RAISED,bg="Green",command=speedcheck)
button.place(x=137,y=360,height=35,width=230) 

speed.mainloop()