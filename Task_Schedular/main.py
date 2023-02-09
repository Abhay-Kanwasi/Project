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

schedule.every().day.at("21:34").do(task)

while True:
    schedule.run_pending()
    tm.sleep(10)

