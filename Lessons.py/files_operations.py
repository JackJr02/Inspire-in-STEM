

#Opening a file
#f=open("lesson1.txt",'x')
f=open("lesson2.txt",'x')

#Read line by line
#print(f.readline())

with open("lesson2.txt",'w',encoding='utf-8') as f:
    f.write("This is my new file/n")
    f.write("It's on a Monday/n")

#Reading The File
print(f.read())
f.close()