#Dictionaries
#!/usr/bin/python

#################
#   Dictionaries
#   Name: Jack Jr
#   Date: 23/05/2022
#################


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