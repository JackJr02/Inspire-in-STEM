#!/usr/bin/python
# Name:Jack Jr
# Date:31/05/2022
# Functions in Python
######################

#Function is a block of code that gets executed together

#Defining a Function
def say_hello():
    print ("Hello from Kenya")
    x=4
    y=7
    z=x+y
    print(z)

say_hello()
###################

def bark():
    print('Dogs bark woof woof!')

def mow():
    print ('Cows mow!')

def neigh():
    print ('Horses neigh!')

bark()
mow()
neigh()
#####################

#Function Parameters
def add_numbers(x,y):
    sum_nums=x+y
    print("The sum of numbers is:",sum_nums)

#Calling the function
add_numbers(40,50)
add_numbers(20,30)
############

def multiply_numbers(x,y):
    prod_nums=x*y
    print('The product of numbers is : ', prod_nums)

multiply_numbers(40,50)
multiply_numbers(20,30)
