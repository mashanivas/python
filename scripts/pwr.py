#!/usr/bin/python

def rp(b, p):
  result = 1
  for i in range(p):
      result = result * b
  return result
n1 = int(input("Enter first number: " ))
n2 = int(input("Enter second number: " ))
print(rp(n1, n2))
