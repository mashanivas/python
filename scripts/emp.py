#!/usr/bin/python
employee_file = open("/home/python/scripts/files/emp.txt", "r")
for employee in employee_file.readlines():
        print(employee)
employee_file.close()
