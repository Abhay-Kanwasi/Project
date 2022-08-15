from tkinter import *
import os

# These function will tell the buttons what actually they want to do..
def restart():
    os.system("shutdown /r /t 1")   # Here 1 means 1 second before restart

def restart_with_time():
    os.system("shutdown /r /t 20")  # Here 20 means 20 second before restart.

def logout():
    os.system("shutdown -l")

def shutdown():
    os.system("shutdown /s /t 1")

# Now first we create a class for calling Tk class of tkinter module.
Command = Tk()
Command.title("Command App")

# Here we create a menu bar

menubar = Menu(Command)
Command.config(menu=menubar)
file_menu = Menu(menubar)
menubar.add_cascade(
    label="Windows Command",
    menu=file_menu
)

Command.geometry("400x300")  # Geometry => width x height
Command.config(bg="#FFFDD0")  # Cream color code => #FFFDD0

# Now we create buttons => 1. Restart   2. Log out   3.Shutdown   4. Restart with time
# 1. Restart
# Here we use relief to make our button a 3D look and we use cursor for what will happen when cursor will arraive to our button.

Restart_Button = Button(Command, text="Restart", font=(
    "Time New Roman", 10, "bold"), relief=RAISED, cursor="plus",command=restart)
Restart_Button.place(x=10, y=10, height=30, width=100)

# 2. Logout

Logout_Button = Button(Command, text="Logout", font=(
    "Time New Roman", 10, "bold"), relief=RAISED, cursor="plus",command=logout)
Logout_Button.place(x=10, y=50, height=30, width=100)

# 3. Restart with time

Restart_with_time_button = Button(Command, text="Restart with Time", font=(
    "Time New Roman", 10, "bold"), relief=RAISED, cursor="plus",command=restart_with_time)
Restart_with_time_button.place(x=10, y=90, height=30, width=150)

# 4. ShutDown

Command_Button = Button(Command, text="ShutDown", font=(
    "Time New Roman", 10, "bold"), relief=RAISED, cursor="plus",command=shutdown)
Command_Button.place(x=10, y=130, height=30, width=100)

# Now we created a Tk object we call a mainloop method which give us a tk titled screen.
Command.mainloop()
