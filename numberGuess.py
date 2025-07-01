#!/usr/bin/env python3
#George Yang
#numberGuess.py

"""
Project Description:
1.	Number guessing 1 - 100 program.
+ Have User1 input a number from 1 - 100
+ check to make sure that user did not cheat or type letters etc.
- Then have User2 guess the number until he/she is correct.
- Gives clue about guessing higher or lower after each guess to help User2.
- Counts how many guesses it took to get the correct answer, and displays that at the end.
- Restarts asking User2 to enter their number now, and repeats for User2.
- I can do this until I type “quit” at any point that gets me out of the program, but the program gives me the option to quit by warning me that I am about to exit y/n.
"""

#ask for input and assign variables. Lets start with User1 name and the mystery number
userOne = input("\nHi! What is your name? ")
print("\nHello "+ userOne +"!")
while True:
    magicNumber = input("Give me a number from 1 to 100: ")
    if 0 <= int(magicNumber) <= 101:
        print("You entered",magicNumber)
        break
    else:
        print("You entered",magicNumber ,"that is not a number between 1-100! Please try again \:\)")

#ok probably do a loop here ^ if whatever entered is not an integer btween 1-100 then ask again?
#find a way later on to also handle input other than integers...


#clear screen
print("\n"*42)

#switch to User2 and ask for their name
userTwo = input("Hi! what is your name? ")
print (userTwo + ", Your friend "+ userOne + " just gave me a number between 1 and 100! Can you guess that number?\n")

# ---Big ass loop here probably

while True:
    guessNumber = input("Give me a guess! ")
    if guessNumber == magicNumber:
        print("\n"*5 + "CONGRATS", userTwo + "!, YOU GUESSED",guessNumber +"WHICH IS CORRECT!" + "\n"*3)
        break
    elif guessNumber < magicNumber:
        print("\nHey",userTwo, "your guess of",guessNumber, "is too low! Try again: " )     
    elif guessNumber > magicNumber:
        print("\nHey",userTwo, "your guess of",guessNumber, "is too high! Try again: " )     
    else:
        print("You entered",magicNumber ,"that is not a number between 1-100! Please try again \:\)")


#or do that in a function inside loop V

#---------OK REVERSE ROLES
#there is probably a more elegant way to do this whole thing in a loop. For now I'll just paste the entire thing over again

#clear screen and prompt 
print("\n"*42 + "OK friends, let's switch roles!" + "\n*4")

#lets do this again...
print("\nHello "+ userTwo +"!")
while True:
    magicNumber = input("Give me a number from 1 to 100: ")
    if 0 <= int(magicNumber) <= 101:
        print("You entered",magicNumber)
        break
    else:
        print("You entered",magicNumber ,"that is not a number between 1-100! Please try again \:\)")

#now for userOne to guess
print (userOne + ", Your friend "+ userTwo + " just gave me a number between 1 and 100! Can you guess that number?\n")

while True:
    guessNumber = input("Give me a guess! ")
    if guessNumber == magicNumber:
        print("\n"*5 + "CONGRATS", userOne + "!, YOU GUESSED",guessNumber +"WHICH IS CORRECT!" + "\n"*3)
        break
    elif guessNumber < magicNumber:
        print("\nHey",userOne, "your guess of",guessNumber, "is too low! Try again: " )     
    elif guessNumber > magicNumber:
        print("\nHey",userOne, "your guess of",guessNumber, "is too high! Try again: " )     
    else:
        print("You entered",magicNumber ,"that is not a number between 1-100! Please try again \:\)")


#------- probably stuff I can use later  VVV
#make a function for wrong input type
def inputTypeCheck():
    #code to check if int between 1-100
    print ("Hey" + userTwo + ", you entered something other than a number! \nPlease try again!")

# -baby loop

#make a function for wrong input & do hi/lo check & give hint
'''
if 
'''

#bool higherThanMagic = ""

'''
def guessWrong():
    print ("Hey" + userTwo +", you entered an the wrong number! \nPlease try again!")
'''

