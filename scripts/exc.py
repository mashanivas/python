#!/usr/bin/python

try:
#    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
     print("Divided by Zero")
except ValueError:
     print("Invalid Error")
