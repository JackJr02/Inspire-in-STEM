#!/usr/bin/python
#################
#   Strings
#   Name: Jack Jr
#   Date: 21/05/2022
#################

#Initializing strings
#Multiline strings

msg="""QRST126XDG MPESA Confirmed 
     you have received ksh 2300 from
     JAMES MUOKI .
     Safaricom TYranparent for you"""""

print(msg)

#Slice From The Start

city="Nairobi"
print (city[:5])

#Slice from the End
print (city[2:])


#Changing from upper to lower and vice versa
f_name ="Ada Lovelace" #Small letters
print (f_name.upper()) #upper() is used to switch from lower case to upper


s_name="LINDA LOVELACE" #CAPITAL LETTERS
print(s_name.lower()) #lower() is used to switch from upper case to lower


#Concatenation
#Is the conversion from one data type to another
#int to float
#float to int
#int to string

number=6
print (str(number))
#6 will be printed as a string

x=4 #4 is an integer
print(float(x))
#4 will be printed as a decimal



