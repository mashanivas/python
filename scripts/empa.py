#!/usr/bin/python
employee_file = open("/home/python/scripts/files/emp.txt", "a")
con = "yes"
while con == "yes":
           in1 = input("Please enter the data entry: ")
           print(in1)
           employee_file.write("\nin1")
           con = input("Enter N to break")
employee_file.close()
