#!/usr/bin/python
# Name:Jack Jr
# Date:02/06/2022
# Classes
######################
#Classes should preferrably start with capital letters

class Person:
    def __init__(self, _name, _age):
         self.name= _name
         self.age=_age
    def sayHi(self):
        print('Hello, my name is ' + str(self.name),'and I am ' + str(self.age), 'years old')
person1=Person('Bob',16)
person1.sayHi()




    