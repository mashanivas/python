#!/usr/bin/python

s = input("Enter a string: ")
print("The string to count is" + s)
count = 1
for s1 in s:
  count += 1
'-' * 35
print("The number of characters in string is: " + str(count))
'-' * 35
print(s.upper())

