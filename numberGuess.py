#!/usr/bin/env python3
#George Yang
#numberGuess.py

"""
######## AI Acknowledgement Statement
- I acknowledge the use of Claude Ai in the couple parts where I needed to clear the screen of the entered number; the prompts used was "how do I clear a terminal in a python command line app" The output given included a bunch of modules and verbose things I didn't learn yet so I just ignored it and ended up printing a bunch of newlines...
########
"""

"""
Project Description:
1.	Number guessing 1 - 100 program.
+ Have User1 input a number from 1 - 100
+ check to make sure that user did not cheat or type letters etc.
+ Then have User2 guess the number until he/she is correct.
+ Gives clue about guessing higher or lower after each guess to help User2.
+ Counts how many guesses it took to get the correct answer, and displays that at the end.
+ Restarts asking User2 to enter their number now, and repeats for User2.
+ I can do this until I type “quit” at any point that gets me out of the program, but the program gives me the option to quit by warning me that I am about to exit y/n.
"""

quit = False
choice = "y"

print("\n\n     GAME OF GUESSES!" + "\n     type quit at any time to quit.")
while True:
    if choice == "y":
        #ask for input and assign variables. Lets start with User1 name and the mystery number
        userOne = input("\nHi! What is your name? ")
        #QUIT OPTION
        if userOne == "quit":
            quit = input("Are you sure you want to exit? Enter \"y\" to quit or anything else to continue :)")
            if quit == "y":
                print("\n"*8, "ok goodbye!", "\n"*4)
                exit()
            else:
                userOne = input("\nOk welcome back! What is your name? ")

        print("\nHello "+ userOne +"!")
        while True:
            magicNumber = input("Give me a number from 1 to 100: ")
            #QUIT OPTION
            if magicNumber == "quit":
                quit = input("Are you sure you want to exit? Enter \"y\" to quit or anything else to continue :)")
                if quit == "y":
                    print("\n"*8, "ok goodbye!", "\n"*4)
                    exit()
                else:
                    magicNumber = ""
            if 0 <= int(magicNumber) <= 101:
                print("You entered",magicNumber)
                break
            else:
                print("You entered",magicNumber ,"that is not a number between 1-100! Please try again :")

        #ok probably do a loop here ^ if whatever entered is not an integer btween 1-100 then ask again?
        #find a way later on to also handle input other than integers...


        #clear screen
        print("\n"*42)

        #switch to User2 and ask for their name
        userTwo = input("Hi! what is your name? ")
        #QUIT OPTION
        if userTwo == "quit":
            quit = input("Are you sure you want to exit? Enter \"y\" to quit or anything else to continue :)")
            if quit == "y":
                print("\n"*8, "ok goodbye!", "\n"*4)
                exit()
            else:
                userTwo = input("\nOk welcome back! What is your name? ")
        print (userTwo + ", Your friend "+ userOne + " just gave me a number between 1 and 100! Can you guess that number?\n")

        # ---Big ass loop here probably
        guessCount = 0
        while True:
            guessNumber = input("Give me a guess! ")
            guessCount += 1
            #QUIT OPTION
            if guessNumber == "quit":
                quit = input("Are you sure you want to exit? Enter \"y\" to quit or anything else to continue :)")
                if quit == "y":
                    print("\n"*8, "ok goodbye!", "\n"*4)
                    exit()
            else:
                magicNumber = ""
                break
            if guessNumber == magicNumber:
                print("\n"*3 + "CONGRATS", userTwo + "!, YOU GUESSED",guessNumber +" WHICH IS CORRECT! you guessed it in",guessCount,"tries!!" + "\n"*3)
                break
            elif guessNumber < magicNumber:
                print("\nHey",userTwo, "your guess of",guessNumber, "is too low! Try again: " )     
            elif guessNumber > magicNumber:
                print("\nHey",userTwo, "your guess of",guessNumber, "is too high! Try again: " )     
            else:
                print("You entered",magicNumber ,"that is not a number between 1-100! Please try again :)")


        #or do that in a function inside loop V

        #---------OK REVERSE ROLES
        #there is probably a more elegant way to do this whole thing in a loop. For now I'll just paste the entire thing over again

        #clear screen and prompt 
        print("\n"*4 + "OK friends, let's switch roles!" + "\n"*4)

        #lets do this again...
        print("\nHello "+ userTwo +"!")
        while True:
            magicNumber = input("Give me a number from 1 to 100: ")
            #QUIT OPTION
            if magicNumber == "quit":
                quit = input("Are you sure you want to exit? Enter \"y\" to quit or anything else to continue :)")
                if quit == "y":
                    print("\n"*8, "ok goodbye!", "\n"*4)
                    exit()
            else:
                print("\nOk welcome back!")
                magicNumber = ''
                break
            if 0 <= int(magicNumber) <= 101:
                print("You entered",magicNumber)
                break
            else:
                print("You entered",magicNumber ,"that is not a number between 1-100! Please try again :)")

        #now for userOne to guess
        print ("\n"*42, userOne + ", Your friend "+ userTwo + " just gave me a number between 1 and 100! Can you guess that number?\n")

        guessCount = 0
        while True:
            guessNumber = input("Give me a guess! ")
            #QUIT OPTION
            if guessNumber == "quit":
                quit = input("Are you sure you want to exit? Enter \"y\" to quit or anything else to continue :)")
                if quit == "y":
                    print("\n"*8, "ok goodbye!", "\n"*4)
                    exit()
            else:
                print("\nOk welcome back!")
                guessNumber = ""
                break
            guessCount += 1
            if guessNumber == magicNumber:
                print("\n"*3 + "CONGRATS", userOne + "!, YOU GUESSED",guessNumber +" WHICH IS CORRECT! you guessed it in",guessCount,"tries!!" + "\n"*3)
                break
            elif guessNumber < magicNumber:
                print("\nHey",userOne, "your guess of",guessNumber, "is too low! Try again: " )     
            elif guessNumber > magicNumber:
                print("\nHey",userOne, "your guess of",guessNumber, "is too high! Try again: " )     
            else:
                print("You entered",magicNumber ,"that is not a number between 1-100! Please try again :)")

        #ask if game continues
        print("Would you guys like to continue this guessing game?")
        choice = input("Enter y to continue, anything else to quit!: ")
        if choice == "y":
            quit = input("Are you sure you want to exit? Enter \"y\" to quit or anything else to continue :)")
            if quit == "y":
               print("\n"*8, "ok goodbye!", "\n"*4)
            else:
                print("\nOk welcome back!")
                break

    else:
        print("\n"*8, "ok goodbye!", "\n"*4)
        break
    




#------- probably stuff I can use later  VVV
#make a function for wrong input type
def inputTypeCheck():
    #code to check if int between 1-100
    print ("Hey" + userTwo + ", you entered something other than a number! \nPlease try again! ")

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

