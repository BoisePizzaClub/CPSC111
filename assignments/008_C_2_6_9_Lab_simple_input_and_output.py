#!/usr/bin/env python3
#George Yang
#008_C_2_6_9_Lab_simple_input_and_output.py



# input a float value for variable a here
a = float(input("Enter variable a: "))
# input a float value for variable b here
b = float(input("Enter variable b: "))
# output the result of addition here
print("The sum of", a, "and", b, "is", a + b)
# output the result of subtraction here
print("the difference of", a, "and", b, "is", a - b)
# output the result of multiplication here
print(a, "multiplied by", b, "is", a * b)
# output the result of division here
#print(a, "divided by", b, "is", a / b)
print("\nThat's all, folks!")

#experiment
try:
    print(a, "divided by", b, "is", a / b)

except ZeroDivisionError:
    print("You tried to divide by zero! Please enter nonzero numbers next time! Goodbye.")
    