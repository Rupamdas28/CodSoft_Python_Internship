import random

print("Welcome Rock,Paper,Scissors game------------------")
user_score=0
comp_score=0
ties=0

name = input("Ener Your Name :")
print("""
Rules of the game:
1.Paper vs Rock ----->Paper
2.Scissors vs Paper ---->Scissors
3.Rock vs Scissors ----> Rock
""")
print()
print()
print("""Choices are:
1.Rock
2.Paper
3.Scissors
""")
while(True):

    ch = int(input("Enter your choice from 1-3::"))
    print()
    while(ch>3 or ch<1):
        ch=int(input("Enter a  valid input"))

    if ch ==1:
        user_choice ="Rock"
    elif ch ==2:
        user_choice="Paper"
    else:
        user_choice="Scissors"

    print("The User's choice is:",user_choice)

    print("Computer's Turn")

    com = random.randint(1,3)

    if com ==1:
        comp_choice="Rock"
    elif com==2:
        comp_choice="Paper"
    else:
        comp_choice="Scissors"

    print("Computer's Choice",comp_choice)

    if ((user_choice=="Paper" and comp_choice=="Rock")or(user_choice=="Rock" and comp_choice=="Paper")):
        print("Wins Paper")
        res = "Paper"
    elif((user_choice=="Scissors" and comp_choice=="Rock")or(user_choice=="Rock" and comp_choice=="Scissors")):
        
        res = "ROck"
    elif(user_choice==comp_choice):
        print("Tie")
        res="Tie"
    else:
        
        res="Scissors"

    if res == "Tie":
        ties=ties+1
    elif res == user_choice:
        print("User Win")
        user_score=user_score+1
    else:
        print("Computer Win")
        comp_score=comp_score+1

    print("Score Board ----------")
    print(name,"score is",user_score)
    print("Computer Score is",comp_score)
    print("Ties are",ties)

    again = input("Play Again ?")
    if (again=="No" or again =="No"):
        break

print("Game Over, Tata")