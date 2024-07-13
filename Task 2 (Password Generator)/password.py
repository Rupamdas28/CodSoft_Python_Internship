
import string
import random
print("Welcome to Random Password Generator---------------------")
def generator():

    length = int(input("Enter the length of password required: "))

    if length < 4:
        print("Minimum password length should be 4 to encompass all character types.")
        return
    print("Creating your password......")

    lowerC = string. ascii_lowercase
    upperC = string. ascii_uppercase
    digitC = string.digits
    symbols = string. punctuation


    password = [
        random. choice(lowerC),
        random. choice(upperC),
        random. choice(digitC),
        random. choice(symbols)
    ]
    com = lowerC + upperC + digitC + symbols
    password += random. sample(com, length - 4)

    random.shuffle(password)
    password = "". join(password)
    print("Your Password :",password)
    generator()

generator()