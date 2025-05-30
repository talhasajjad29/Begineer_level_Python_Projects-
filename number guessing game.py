""" Number Guessing Game (Using Functions)
🔧 Features:
User has to guess a randomly generated number.
Counts attempts.
Option to play again"""


import random
def welcome():
    print("\nWELCOME to number guessing game\nNumber between 1 to 100\nLets TRy to GUESS!\n")

def user_input():
    while True:
        try:
            guess=int(input("Enter number between 1 to 100:"))
            if 1<=guess<=101:
                return guess
            else:
                print("Plz enter number between 1 to 100:")
        except ValueError:
            print("Enter numeric value!!")  

def main():
    welcome()
    r_no=random.randint(1,100)
    count=1
    while True:
        user_guess=user_input()
        if r_no==user_guess:
            print("Hurrah! You guessed right!!")
            break
        elif r_no>user_guess:
            print("Close!! Your number is small!")
        else:
            print("Close!! Your number is large!")     
        count+=1
    print(f"You guessed number in {count} attempt{'s' if count > 1 else ''}")

def playagain():
        while True:
            again=input("Want to playagain(y/n)?").lower()
            if again in ["y","n"]:
                return again=="y"              
        
while True:                               
    main()
    if not playagain():
        print("!! Good Bye !!")
        break
        
