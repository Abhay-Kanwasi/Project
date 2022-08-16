# Typing Speed Calculator

# Importing required modules
from time import *
import random as r

# This function check the errors in user inputted string.
def error(paragraph_test,user_test):
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
if __name__ == '__main__':
    while True:
        check = input("ready to test : yes/no : ")
        if check == "yes" or check == "Yes":
            text = ["A Charmender is a fire type pokemon",
                    "A Pikachu is a lightning type pokemon",
                    "Raichu is the advance version of Pikachu"
                    ] 
            print("******** Typing Speed Calculator ***********")
            print()
            string = r.choice(text)
            print(f"Type this : {string}")
            print()

            time1 = time()
            testinput = input("Enter : ")
            time2 = time()
            print()
            print('Speed :',typing_speed(time1,time2,testinput),"word/sec.")
            print()
            print("Error :",error(string,testinput))
            print()
        elif check == "no" or check == "No":
            print()
            print("Thank you for checking..")
            break

        else:
            print()
            print("Wrong input.")
