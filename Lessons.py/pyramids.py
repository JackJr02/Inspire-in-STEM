rows= int (input("Enter number of rows"))
for i in range (rows):
    for j in range (i+1):
        print("*", end=" ")
    print("\n")

row=int(input("Enter number of rows"))
for i in range (rows):
    for j in range (i+1):
        print(j+1,end=" ")
    print("\n")