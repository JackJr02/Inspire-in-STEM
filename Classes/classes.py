#!/usr/bin/python
# Name:Jack Jr
# Date:02/06/2022
# Classes
######################

class person:
    def _init_(self, _name, _age):
             self.name= _name
             self.age=_age
    def sayHi(self):
        print('Hello, my name is' + str(self.name),'and I am' + str(self.age), 'years old')
person1=person("Bob",str(16))
person1.sayHi()

    