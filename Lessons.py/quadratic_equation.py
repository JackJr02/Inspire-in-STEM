#!/usr/bin/python
# Name:Jack Jr
# Date:31/05/2022
# Solving quadratic equations
######################

import math
a=int(input("Enter the coefficient of first term"))
b=int(input("Enter the coefficient of the second term"))
c=int(input("Enter the constant"))

def find_roots(a,b,c):
     y1=((-b+ math.sqrt((b**2)-4*a*c))/2*a)
     y2=((-b- math.sqrt((b**2)-4*a*c))/2*a)
     print ("The roots of the quadratic equation are :",y1,y2)
find_roots(a,b,c)