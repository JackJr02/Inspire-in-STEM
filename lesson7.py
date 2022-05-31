#Lists

from calendar import monthrange
from pydoc import plain
from socket import MSG_DONTROUTE

motorcycle_owner= "MojoJojo"
plate_number=["_d123", "_y123", "_b123", "_h123"]
motorcycles=["ducati","yamaha","boxer","honda"]
print(motorcycles [0] + str ( plate_number[0]),motorcycles [1] + str( plate_number[1]), motorcycles[2] + str( plate_number[2]), motorcycles[3] + str( plate_number[3] ) )
print (f"My name is { motorcycle_owner} and I own motorcycle plate number {plate_number[0]}")


#Accessing List Items using the Index

print (motorcycles[-1])

#Changing Elements In a List

motorcycles[0]="bugatti"
print (motorcycles)
print ("I love" + str ( motorcycles[0]))

#Adding Elements in a List(.append)

motorcycles.append ("ktm")
print(motorcycles)

#Deleting an Item from a List(del)
del motorcycles[0]
print (motorcycles)

#Pop() method is used to delete the first item
popped_motorcycles = motorcycles.pop()

#Remove() method
motorcycles.remove ("yamaha")
print (motorcycles)

