#!/usr/bin/env python3
#George Yang
#003_C_2_3_3_operators.py


print("\n"*4)
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

print("\n"*3)

range=int(input("Enter a range in kilometers between 150-400 for your target!\t"))
#15 ish minutes flight time for maybe 400km?
timeFlightTotalMin=(range/400)*15
timeFlightTotalSec=timeFlightTotalMin*60
print("\nThe total flight time is probably", timeFlightTotalMin, "minutes....")

#assume some wierd decceleration guesstimate
timeFlightTerminal=(80*1000/mps) #km to m
print("The critical time is probably the last 80 or so kilometers; it may only span", timeFlightTerminal, "seconds!")

#so in the span of 48 seconds, the interceptor possibly as 1/3 of that time as a window
windowOfIntercept=timeFlightTerminal/3

print("\nThe window of intercept is probably", windowOfIntercept, "seconds..")
#ok so 16 seconds. Did the systems back in the 90's allow for the warhead itself to do the computing? probably not. 24-bit fixed sounds like something out of the 60s and the warhead itself is pretty small.

#New code for cheesy radar onboard missile lets say resolution of only 1/2 second vs 1/10
resolutionInterceptor= windowOfIntercept*2 #half seconds
print("\nThe interceptor has about", resolutionInterceptor, "ticks to process a bunch of stuff!! \n each tick it will process its distance to target and adjust angle of attack\nwith the radar and computational aspect being negligible")

#32 ticks
#26.67km window for target travel
closeInWindow=26667/(686+1676) #mach 2 is 686 m/s
ticks=closeInWindow*2
print("\nThe two objects flying together will collide in ", closeInWindow, "seconds or", ticks, "ticks")

#down to 22 usable ticks
def tickMath(ticks):
    i=0
    fuzzy=26667
    while i<=ticks:
        finalDist=fuzzy-(i*(686+1676)/2) #mach 2 is 686 m/s
        print("T-", (22-i)/2,"seconds, The distance to target is:", finalDist, "meters!")
        i+=1
    return finalDist

print("Ok so generally this missile radar will only see ", (58/50)*tickMath(22)-tickMath(22), "meters remaining!")

#this method has a pretty significant error of 110m compared to the actual ground controll Patriot system of 1991 of hundres! But if the radar on the interceptor also processed at the same of 1/10 second then the error distance could be minimized 

print("lets try this with a similar resolution of 1/10th sec instead!")

resolutionInterceptor= windowOfIntercept*10 #tenth seconds
closeInWindow=26667/(686+1676) #mach 2 is 686 m/s
ticks=closeInWindow*10
print("\nThe two objects flying together will collide in ", closeInWindow, "seconds or", ticks, "ticks")

def tickMath(ticks):
    i=0
    fuzzy=26667
    while i<=ticks:
        finalDist=fuzzy-(i*(686+1676)/10) #mach 2 is 686 m/s
        print("T-", (113-i)/10,"seconds, The distance to target is:", finalDist, "meters!")
        i+=1
    return finalDist

print("now this missile radar will only see ", tickMath(113), "meters remaining!")

#maybe a better approach would be a transciever on the missile, so the missile did the actual radar tracking after a much more rough directional launch, and would relay the raw data back to the launcher vehicle for computation. The onboard radar would possible have a range of at least multiple kilometers so the launcher wouldn't need to track with such sensitivity throughout the terminal phase of the target when the target is at the maximum velocity. I'm guessing the interceptor radar can be much more loud and with a smaller angle to listen to so losing track of the target would be very difficult, versus a ground based system that is staring at presumably a large third of the sky.




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