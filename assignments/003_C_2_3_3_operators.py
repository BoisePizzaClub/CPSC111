#!/usr/bin/env python3
#George Yang
#003_C_2_3_3_operators.py

#ok lets try something! 
print("the range of numbers represented by a 24-bit fixed point format,\n if each integer represents a tenth of a second is probably", (2**24-1)/36000, "hours")  #pemdas 

#that holds a lot of hours, 20 days+ so the problem was something else. Lets try some simple math using trickery. Stick with small integers but separate the timestamps into the integer seconds, and the tenths as another integer

#convert scud to meters per second
print("the scud travels ",3750, "miles per hour, which converts to"  ) #ok trickery begins
mph=3750

#going to convert to miles per second first to start with enormous number
mips=3750/3600
print(mips, "miles per second!") #I'm going to manually integer divide this and look at the modulo

mps=mips*1600.344
mpts=(mps/10)

print("or,",mpts, "meters per tenth second")
# Now lets put it back in and see if we get close to 3750

newMPH=mpts*10*3600/1600.344

print("ok after all this, it converts back to", newMPH,"miles per hour.")
#hmm is that 1676m/s

#alright lets throw some real world time and velocity into this.

range=int(input("Enter a range in kilometers between 150-400 for your target!\t"))
#15 ish minutes flight time for maybe 400km?
timeFlightTotalMin=(range/400)*15
timeFlightTotalSec=timeFlightTotalMin*60
print("The total flight time is probably", timeFlightTotalMin, "minutes....")

#assume some wierd decceleration guesstimate
timeFlightTerminal=timeFlightTotalSec/mps


"""
Module 02 Lecture 01
What is...
A. 00000001 +1 = __________ in binary?
    10
B. 00001111 + 1 = ___________ in binary?
    00010000
C. 0x000F + 1 = ____________ in hexadecimal?
    0x0010
D. 0x0009 + 1 =  ____________ in hexadecimal?
    0x000A
Module 02 Lecture 02
A. How do we remember the order of operations in Python math?
    PEMDAS.
B. What are three things to remember when creating variables?
    cannot be a python keyword, variables are case sensitive, must begin with a letter and 
    only use _ not spaces.
C. Write an input statement that converts the answer to a decimal point number
    number=float(input("Input a number!\t"))
"""