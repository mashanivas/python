#!/usr/bin/python
try:
   number1 = float(input("Enter first number: "))
   number2 = float(input("Enter second number: "))
   sum = number1 + number2
   print("The first number: " + str(number1))
   print("The first number: " + str(number2))
   print("The SUM is: " + str(sum))
except:
   print("Invalid Input")
