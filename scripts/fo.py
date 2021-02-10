#!/usr/bin/python

employee_file  = open("files/emp.txt", "w")
#for employee in employee_file:
#   print(employee.readline())
#for employee in employee_file.readlines():
# print(employee)
#print(employee_file.read())
employee_file.write("\nToby - Human Resources")
employee_file.close()
