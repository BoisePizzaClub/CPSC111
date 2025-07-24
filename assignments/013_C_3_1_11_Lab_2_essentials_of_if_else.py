#!/usr/bin/env python3
#George Yang
#013_C_3_1_11_Lab_2_essentials_of_if_else.py

income = float(input("Enter the annual income: "))

if income <= 0:
	tax = 0.
elif 0 < income < 85528:
	tax = income * 0.18 - 556.02
elif income >=85528:
	tax = 14839.02 + (85528 - income) * 0.32

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
