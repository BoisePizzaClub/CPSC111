#!/usr/bin/env python3
#George Yang
#010_C_2_6_11_Lab_operators_and_expressions2.py

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

startTimeMinutes = hour * 60 + mins #convert start time to minutes

endTimeMinutes = startTimeMinutes + dura

endHours = endTimeMinutes // 60

endMinutes = endTimeMinutes % 60


print("The event started at ", hour, ":", mins, " and ended at ", endHours ,":", endMinutes , sep="")
