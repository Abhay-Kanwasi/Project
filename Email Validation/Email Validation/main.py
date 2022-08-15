# Email Velidation (Check wheather entered email is correct or not.)

def email_validation(email):
    d,j,k = 0,0,0  # For condition 5

    # There are many conditions to check email velidation.

    # Condition 1 : Minimum length of the email is 6.
    if len(email) >= 6:

        # Condition 2 : The first letter of email must be a smallcase character.
        
        if email[0].isalpha():
        
            # Condition 3 : One '@' must be present in email.
            if ("@" in email) and (email.count("@")==1):

                # Condition 4 : '.' must be present in the email in 3rd or 4th position.
                if (email[-3] == '.') ^ (email[-4] == '.'): # We use XOR operator here because if both the conditions are true then we get two '.' in our email which is also invalid.

                    # Condition 5 : No wide space allow in email and all the characters in email must be in lowercase.
                    for i in email:
                        if i == i.isspace():
                            k += 1
                        elif i.isalpha():
                            if i == i.upper():
                                j += 1
                        elif i.isdigit():
                            continue
                        elif i == '_' or i == '.' or i == '@':
                            continue
                        else:
                            d += 1
                        
                    if k == 1 or j == 1 or d == 1:
                        print("Wrong Email. Spaces are not allow in email name.\nUppercase letter also not allowded into email name.")
                    else:
                        print("Valid Email")

                else:
                    print("Wrong email. Full stop position must be inputed wrong.")
            
            else:
                print("Wrong email. One '@' must present in the email.")
        
        else:
            print("Wrong email. First letter of the email must be a letter.")

    else:
        print("Wrong email. Email must be of atleast 6 character.")        


email = input("Enter your email : ")
email_validation(email)
