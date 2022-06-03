import random
print("Welcome to our Password Generator")
character='Smokemon222'
#Asking number of passwords to be generated
num_passwords=input("Enter number of passwords to be generated ")
#Converting the number of passwords into integers
num_passwords=(int(num_passwords))
#Ask user for password length
len_password=input("How many characters should the password have? ")
#Convert password lenghts into integers
len_password=(int(len_password))

print("\n Here are your passwords")

for password in range (int(num_passwords)):
    password=''
    for c in range (int(len_password)):
             password+=random.choice(character)
print(password)