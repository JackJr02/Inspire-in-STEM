#!/usr/bin/python
#################
#   File: main.py
#   Name: Jack Jr
#   Date: 06/06/2022
#################

import operations
from students import student
from teachers import teachers

print(operations.add_numbers(3,5))
print(operations.subtract_numbers(8,6))
print(operations.divide_numbers(10,2))

new_student=student("Sam","cycling",2012)
new_student.greet_student()

new_teacher=teachers("Mr Calvin",12908,"Literature",40000)
new_teacher.get_tsc_no()
print(new_teacher.get_tsc_no)
