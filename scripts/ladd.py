#!/usr/bin/python
# Program to add the minimum positive number greater than 1 t an array
# Array definition
U1=[-200, -500, 0, 2, 4, 5, 500, 2000, 3000]
U1.sort()
# Printing an existing array
'+' * 55
print("Existing sorted array is: ", U1)
'+' * 55
# Initialize a variable for comparision
c1 = 2
# For loop to check if c1 is in the array and if doesn't exist append the array
for n in U1:
    if c1 in U1:
       c1 += 1
#       print(c1)
       continue
    else:
       U1.append(c1)
       U1.sort()
# Printing out the updated array with a lowest number added
       '+' * 55
       print("Added an array member: ", c1)
       print("The new array is: ", U1)
       '+' * 55
       break
