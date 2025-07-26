#!/usr/bin/env python3
#George Yang
#014_C_3_1_12_Lab_3_essentials_of_if_elif_else.py

year = int(input("Enter a year: "))
type = ""

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
    #  Write the if-elif-elif-else block here.
	if year % 4 != 0:
		print("The year", year, "is a common year.")
	elif year % 100 != 0:
		print("The year", year, "is a leap year.")
	elif year % 400 != 0:
		print("The year", year, "is a common year.")
	else:
		print("The year", year, "is a leap year.")
		
#print("The year", year, "is a common year.")
#print("The year", year, "is a leap year.")

#experiment failed, wrong logic and prints excess line..

# year = int(input("Enter a year: "))
# type = ""

# if year < 1582:
# 	print("Not within the Gregorian calendar period")
# else:
#     #  Write the if-elif-elif-else block here.
# 	if year % 4 != 0:
# 		type = "common"
# 	elif year % 100 != 0:
# 		type = "leap"
# 	elif year % 400 != 0:
# 		type = "common"
# 	else:
# 		type = "leap"
# print("The year", year, "is a", type, "year.")
