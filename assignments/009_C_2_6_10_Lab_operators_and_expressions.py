#!/usr/bin/env python3
#George Yang
#009_C_2_6_10_Lab_operators_and_expressions.py

x = float(input("Please enter a positive nonzero number: "))  #enter the number

d = x + 1 / x   #PEMDAS
c = x + 1 / d
b = x + 1 / c
a = 1 / b

print("After processing the number", x, ", we obtain", a)

#experiments below