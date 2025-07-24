#!/usr/bin/env python3
#George Yang
#010_C_2_6_11_Lab_operators_and_expressions2.py

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

elapsedHours = dura // 60 + hour
elapsedMinutes = dura % 60

print("The even ended at", elapsedHours,":", elapsedMinutes)
