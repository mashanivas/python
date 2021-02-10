#!/usr/bin/python
# Python function to add minimum value to an array
# Initialized array
U1=[-200, -500, -122, 800, -899]
# Value determination using for and if conditions
def numaddmin(U1):
 # Let us sort this
 U1.sort()
 # Adding lines for readability
 '+' * 55
 print("Existing sorted array is: ", U1)
 '+' * 55
 # Min function to determine the minimum from the array
 c1 = min(U1)
 # Comparision to determine sign
 if c1 < 0:
   c1 = -1
 else:
   c1 = 1
 for n in U1:
    if c1 in U1:
       c1 += 1
#       print(c1)
       continue
    else:
       U1.append(c1+min(U1))
       U1.sort()
#Printing the output with the value added to the array
       '+' * 55
       print("Added an array member: ", min(U1))
       print("The new array is: ", U1)
       '+' * 55
       break
       return U1

numaddmin(U1)
U2 = [-19, -30, -100, -300, 0, 1, 2, 4, 76, 890, 999, 9999, 11111]
numaddmin(U1)
