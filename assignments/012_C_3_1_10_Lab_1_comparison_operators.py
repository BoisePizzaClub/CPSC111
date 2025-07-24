#!/usr/bin/env python3
#George Yang
#012_C_3_1_10_Lab_1_comparison_operators.py

#input section
answer = input("What is the best plant ever?")

#conditions
if answer == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif answer == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not ", answer,"!",sep="")
