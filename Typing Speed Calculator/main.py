# Typing Speed Calculator

# Importing required modules
from time import *
import random as r

# This function check the errors in user inputted string.
def mistake(paragraph_test,user_test):
    error = 0
    for i in range(len(paragraph_test)):
        try:
            if paragraph_test[i] != user_test[i]:
                error = error + 1
        except:
            error = error + 1
    return error

# This function will check the typing speed
def typing_speed(time_start,time_end,user_input):
    time_delay = time_end - time_start
    time_roundoff = round(time_delay,2)
    speed = len(user_input)/time_roundoff
    return round(speed) 


# MAIN PROGRAM

print("******** Typing Speed Calculator ***********")

text = ["A Charmender is a fire type pokemon",
        "A Pikachu is a lightning type pokemon",
        "Raichu is the advance version of Pikachu"
        ] 

string = r.choice(text)
print(f"Type this : {string}")
print("\n\n")

time1 = time()
testinput = input("Enter : ")
time2 = time()

print('Speed :',typing_speed(time1,time2,testinput),"word/sec.")
print("Error :",mistake(string,testinput))
