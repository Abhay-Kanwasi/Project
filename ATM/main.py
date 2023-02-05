import time
print("\nWelcome to Bank of AK Production ATM\n ")
time.sleep(2)
restart = ('Y')
chances = 3
balance = 10000.12
while chances >= 0:
    pin = int(input('\nEnter your 4 digit pin : '))
    time.sleep(2)
    if pin == (1234):
        print("\nYou entered the pin correctly.\n")
        time.sleep(2)
        while restart not in ('n','No','NO','N'):
            print("Press 1 : Check Balance\n")
            print("Press 2 : Cash Withdrawl\n")
            print("Press 3 : Pay in\n")
            print("Press 4 : Return Card\n")
            option = int(input("Choose your option : "))
            time.sleep(2)
            if option == 1:
                print("Your balance is Rs.",balance,'\n')
                restart = input("Press Y to restart.\nPress N to exit.\nChoose : ")
                if restart in ('n','No','NO','N'):
                    print("Thank You ! Have a good day.")
                    exit()
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input("for other options enter 1.\nEnter the amount : "))
                if withdrawl > balance:
                    print("Invalid amount.")
                balance = balance - withdrawl
                print("Your balance : ",balance)
                restart = input("Go Back\nPress Y to restart.\nPress N to exit.\nChoose : ")
                if restart in ['n','N','NO','no','No']:
                    print("Thank You !")
                    exit()
                elif withdrawl == 1:
                    withdrawl = float(input("Enter the amount : "))
            elif option == 3:
                Pay_in = float(input("Enter the amount you want to pay in : "))
                balance += Pay_in
                print("New balance : ",balance)
                restart = input("Press Y to restart.\nPress N to exit.\nChoose : ")
                if restart in ('n','No','NO','N'):
                    print("Thank You ! Have a good day.")
                    exit()
            elif option == 4:
                print("Please wait...\n")
                time.sleep(3)
                print("Card Succesfully discarded..\n")
                print("Greatful for your services.")
                exit()
            else:
                print("Please enter the correct number.\n")
                restart = ('y')
    elif pin != ('1234'):
        print("Incorrect password !")
        time.sleep(3)
        chances = chances - 1
        if chances == 0:
            print("Today's trying limit exceed..\n")
            time.sleep(2)
            print("Try after 24 hours...")
            break



            