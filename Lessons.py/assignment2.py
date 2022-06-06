for number in range (0,9):
    print(number)

#Print a pyramid of stars
rows=int(input("Enter the number of rows"))
for i in range(rows):
    for j in range (i+1):
        print("*",end = " ")
        print("\n")
        

#Print a diamond of stars
print("\t\t\t",number,"\t\t\t")
print("\t\t\t",number**2,"\t",number**2,"\t")
print("\t",number**2,"\t",number**2,"\t",number**2,"\t",number**2,"\t",number**2)
print(number**2,"\t",number**2,"\t",number**2,"\t",number**2,"\t")
print("\t",number**2,"\t",number**2,"\t\t",number**2,"\t",number**2,"\t",number**2,"\t")
print("\t\t",number**2,"\t",number,"\t",number**2)
print("\t\t\t",number,"\t\t\t")
