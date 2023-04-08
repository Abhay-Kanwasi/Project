import schedule
import time as tm
from datetime import time, timedelta,datetime
from plyer import notification
from time import sleep

def task():
    notification.notify(
        title = " Take a Rest ",
        message = " Don't take too much strain it's easy if you will takea break.\nIt's good for your mental health.\nIt increaseconcentration and memory.",
        app_icon = "C:/Users/djoke/Desktop/Project/Desktop Notifier/Icon.ico",
        timeout = 1
    )

# Method 1

time = input("Enter the time in (HH:MM) format : ")
day_counter = int(input("How many days you want this notification : "))
j = schedule.every().day.at(time).do(task)

count = 0
while True:
    schedule.run_pending()
    tm.sleep(10)
    count += 1
    if count == day_counter:
        schedule.cancel_job(j)

