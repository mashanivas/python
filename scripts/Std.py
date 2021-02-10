#!/usr/bin/python
from Student import Student

student1 = Student("Tim","Business", 3.1, False)
student2 = Student("Tom","Art", 3.6, True)
# print(student1)
print(student1.on_honor_role())
print(student2.on_honor_role())
