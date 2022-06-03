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
############

#Using Default Parameters
def print_name(name="Jack Jr"):
    print(name)

print_name("Yourself")

#Return from a Function
def get_sum(num1,num2):
    sum_num=num1+num2
    return sum_num
print(get_sum(7,12))

def get_square(num1,power):
    squares=num1**power
    return squares
print(get_square(6,4))
##########

#
def get_full_name(f_name,s_name):
    full_name=f_name + " " + s_name
print(get_full_name("Jack","Jr"))
##########

#Returning a Dictionary from a Function
def create_full_name(first_name, second_name):
    person=("'first':first_name,'second':second_name")
    return person

student=create_full_name('Jack','Jr')
print (student)
###########

#Passing a List in a Function
def greet_friends(names):
    for name in names:
        msg="Hello " + name.title()+ "!"
        print(msg)
friends=['Brook','Tevo','Farmacy','Bickey']
greet_friends(friends)


