#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     02/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import string
import random

def generate_password(length,special_char=False):
    char =string.ascii_letters + string.digits
    if special_char:
        char +=string.punctuation
    password ="".join(random.choice(char)for _ in range(length))
    return password

def main():
    print("_________Password Generator________")

    try:
        length= int(input("Enter Your desired password length:"))
        special_char=input("Do U want to add Specisl Charachter: (yes/no)\n").lower()=='yes'
        if length<=0:
          print("Enter Positive Number")
        else:
            password=generate_password(length,special_char)
            print("Your Generated Password\n",password)

    except:
        print("Invalid Input")


if __name__ == "__main__":
    main()
