#!/usr/bin/python
# Program to add a maximum number to an existing array
U1=[-200,-5,-2,0,1,2,4,5,6,7,8,9,10,11,15,20,45,89]
# Let us sort and print an existing array
U1.sort()
'+' * 55
print("Existing sorted array is: ", U1)
'+' * 55
# Function to determine the maximum value
c1 = max(U1)
# For loop to check if exists in loop increment or append 
for n in U1:
    if c1 in U1:
       c1 += 1
       continue
    else:
       U1.append(c1)
       U1.sort()
# Print the final values
       '+' * 55
       print("Added an array member: ", c1)
       print("The new array is: ", U1)
       '+' * 55
       break
