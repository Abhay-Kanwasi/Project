# EMAIL VALIDATION USING REGEX

import re

while True:
    email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    user_email = input("Enter the email : ")
    if re.search(email_condition,user_email):
        print("Valid Email")
    else:
        print("Wrong Email")