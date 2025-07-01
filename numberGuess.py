#!/usr/bin/env python3
#George Yang
#numberGuess.py

"""
Project Description:
1.	Number guessing 1 - 100 program.
- Have User1 input a number from 1 - 100
- check to make sure that user did not cheat or type letters etc.
- Then have User2 guess the number until he/she is correct.
- Gives clue about guessing higher or lower after each guess to help User2.
- Counts how many guesses it took to get the correct answer, and displays that at the end.
- Restarts asking User2 to enter their number now, and repeats for User2.
- I can do this until I type “quit” at any point that gets me out of the program, but the program gives me the option to quit by warning me that I am about to exit y/n.
"""

#ask for input and assign variables. Lets start with User1 name and the mystery number
str userOne = input("Hi! What is your name?")
int magicNumber = input("Hello "+userOne, "give me a number between 1 and 100")
#ok probably do a loop here ^ if whatever entered is not an integer btween 1-100 then ask again?

#switch to User2 and ask for their name
str userTwo = input("Hi! what is your name?")
print "Your friend "+ userOne + " Just gave me a number between 1 and 100! Can you guess that number?"

# ---Big ass loop here probably
'''
This following part is going to be more type checking
Probably 

str guessRaw = input("Type a number between 1-100:")
if string is not an int
    if string is not 
'''

##or do that in a function inside loop V

#make a function for wrong input type
def inputTypeCheck():
    #code to check if int between 1-100
    print "Hey" + userTwo + ", you entered something other than a number! \nPlease try again!"

# -baby loop

#make a function for wrong input & do hi/lo check & give hint
'''
if 
'''

bool higherThanMagic = ""

def guessWrong():
    print "Hey" + userTwo +", you entered an the wrong number! \nPlease try again!"


#make a function for wrong guess

# ---even bigger loop lol

