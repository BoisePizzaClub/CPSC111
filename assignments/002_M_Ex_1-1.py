#!/usr/bin/env python3
#George Yang
#002_M_Ex_1-1.py

#Ok I made a mistake and did the wrong assignment. Doing the actual Murach "Future Value program" now

#Murach code below VVV future_value_errors.py
import locale

# set the locale for use in currency formatting
locale.setlocale(locale.LC_ALL, 'en_US')

"""
# display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":

    # get input from the user
    monthly_investment = float(input("Enter monthly investment:\t"))
    yearly_interest_rate = float(input("Enter yearly interest rate:\t"))    #FIRST ERROR missing )
    years = int(input("Enter number of years:\t\t"))

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12  #SECOND ERROR year is undefined, try years

    # calculate the future value
    future_value = 0
    for i in range(months):
        future_value = future_value + monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value = future_value + monthly_interest_amount

    # format and display the result
    print("Future value:\t\t\t" + locale.currency(
        future_value, grouping=True))
    print()

    # see if the user wants to continue
    choice = input("Continue? (y/n): ")
    print()

print("Bye!")
"""
"""ok this runs fine, but the user experience is unclear... what is the interest rate?
percentage or decimal?
therefore this would be better off with more clarity
"""

#George's experiments: ok I'm going to modify this to be more user friendly.

choice = "y"
while choice.lower() == "y":

    # get input from the user
    monthly_investment = float(input("Enter monthly investment:\t\t"))
    yearly_interest_rate = float(input("Enter yearly interest rate percent:\t"))
    #[G] add clarity with feedback
    print("Ok, you entered an investment of\t",monthly_investment, "\n\twith an interest rate of\t", str(yearly_interest_rate) + "%")
    years = int(input("Enter number of years:\t\t\t"))

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0
    for i in range(months):
        future_value = future_value + monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value = future_value + monthly_interest_amount

    # format and display the result
    print("Future value after",years, "year(s):\t\t" + locale.currency(
        future_value, grouping=True))
    print()

    # see if the user wants to continue
    choice = input("Continue? (y/n): ")
    print()

print("Bye!")