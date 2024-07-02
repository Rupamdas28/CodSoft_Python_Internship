print("Welcome to Calculator----------------------------")
a = float(input("Enter a Number :"))
b = float(input("Enter another Number:"))

print("1->Addition +")
print("2->Substraction -")
print("3->Multipication *")
print("4-> Division /")
print("5-> Modulas %")
print("6-> Exit")



while(True):
    c = int(input("Enter your want to perform:"))
    if (c==1):
        print("The Addition is:",a+b)
    elif(c==2):
        print("The Substraction is:",a-b)
    elif(c==3):
        print("The Multipicatin is:",a*b)
    elif(c==4):
        print("The Division is:",a/b)
    elif(c==5):
        print("The Modulas is:",a%b)
    elif(c==6):
        print("Exiting")
        break
    else:
        print("Invalid Input")