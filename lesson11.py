#!/usr?bin/python

##########
# Name: Jack Jr
# Date: 26/05/2022
##########

for number in (range(0,20)):
    print(number)
for number in (range(0,20)):
    if(number%2==0):
        print(number)

#Sum of Even Numbers between 0 and 20
sum=0
for number in (range(0,20)):
    if (number%2==2):
        sum=sum + number
        print(sum)

#Sum of Product of odd numbers between 0 and 50
prod_num=1
for number in range (0,50):
    if (number%2==1):
        prod_num=prod_num + number
        print (prod_num)
