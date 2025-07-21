#!/usr/bin/env python3
#George Yang
#005_C_2_4_9_Lab_1_variables.py

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#experiments

#USD to SGD and CHF converter
#rate at 1 SGD = 0.779535 USD and 1 CHF = 1.25019 USD
# usd = 9449.
# sgd = usd / 0.779535
# chf = usd / 1.25019
# print(usd, "USD is", round(sgd, 2),"SGD", "and", round(chf,2),"CHF")

#F to C and K converter
#conversion of C = (F - 32) / 1.8 and K = C + 273.15
# f = 67.
# c = (f - 32)/1.8
# k = c + 273.15
# print(f, "Farenheit =", round(c,1),"Celsius, and ", round(k,1), "Kelvin")
