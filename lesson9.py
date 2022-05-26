#Dictionaries
#!/usr/bin/python

#################
#   Dictionaries
#   Name: Jack Jr
#   Date: 23/05/2022
#################

#Dictionary is a collection of key valued pairs
#Inside it is a key and value
#Dictionary Syntax:['key':'value']
#Curly braces {} are used 

colors={'color':'red'}
vehicle={'type':'toyota','plate number':'KYZ234'}
print(colors)
#We use the type() method to read the data type
print (type(colors))
#########
#Printing vehicle type and plate number
print(vehicle['type'],vehicle['plate number'])

#Accessing values in a dictionary
print (vehicle['type'])
#########

#Dictionary of a person
person={'name':'Ada','age':'20','id_no':'39684550','phone_number':'0731678905'}
print(person)
person['gender']='female'
print(type(person))
del person['phone_number']
print (person)
##########

#Looping over dictionaries
for Key, value in person.items



#Initializing dictionaries
student = {"name":"Jack", "age":20, "grade": 'B+'}
print (student)

#Adding Key values in Dictionaries
student ["id"]=2222
student ["hobby"]="Reading novels"
print (student)

#Starting with an Empty Dictionary
student = {}


#Initializing an Empty Dictionary
student = {}
student ["home_city"]="Nairobi"
student ["fav food"]="Chapati"
print (student)

#Modifying Values
student ["fav food"]="Pizza"
print (student)


#Removing key value pairs (del is used)
del student ["fav food"]
print (student)