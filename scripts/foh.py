#!/usr/bin/python

employee_file  = open("files/emp.html", "w")
#for employee in employee_file:
#   print(employee.readline())
#for employee in employee_file.readlines():
# print(employee)
#print(employee_file.read())
employee_file.write("\n<p> This is html </p>")
employee_file.close()
