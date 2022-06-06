#!/usr/bin/python
#################
#   Strings
#   Name: Jack Jr
#   Date: 21/05/2022
#################


#String Methods
#Methods are In built functions used to work on all the different data types
#\n is used for new lines
#\t is used for new tabs

name="JackJr"
age=20
user_name=" Ada Lovelace"

print("My name is {} and I am {} years old".format(name,age))

#The Format Method(f)
#Syntax
#(f"Declared variables")
print (f"My name is {name} and I am {age} years old")


#The Strip Method
#Strips out whitespaces
#rstrip() strips the right side
#lstrip() strips the left side
print (user_name.strip())


#The replace() method replaces a character/string with another
name= "Ada Lovelace"

print(name.replace('A','I'))
print(name.replace("Ada", "Linda"))


#The split() method splits sentences into single words hence a list
msg="Ada Lovelace was the first known programmer"

print(msg.split())


#The len() method is used in getting the lenght of a string
print (len(msg))
