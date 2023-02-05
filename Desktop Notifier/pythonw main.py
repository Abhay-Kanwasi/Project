# File name changed because we want to run it in desktop background.
# pythonw <file name>.py

from plyer import notification
from time import sleep

while True:
    notification.notify(
        title = " Take a Rest ",
        message = " Don't take too much strain it's easy if you will takea break.\nIt's good for your mental health.\nIt increaseconcentration and memory.",
        app_icon = "C:/Users/djoke/Desktop/Project/Desktop Notifier/Icon.ico",
        timeout = 5
    )
    sleep(10) # Every notication will wait 10 second. 