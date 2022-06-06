#!/usr/bin/python
#################
#   Operations
#   Name: Jack Jr
#   Date: 06/06/2022
#################
def add_numbers(x,y):
    result=x+y
    return result

def subtract_numbers(x,y):
    result=x-y
    return result

def divide_numbers(x,y):
    result=x/y
    return result
    
class students:

    def __init__(self,name,hobby,year_of_birth):
        self.name=name
        self.hobby=hobby
        self.year_of_birth=year_of_birth
    def greet_student(self):
        print("Hello from " + self.name)
