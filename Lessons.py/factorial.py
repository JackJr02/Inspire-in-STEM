number=input("Enter number")
number=int(number)
factorial=1
if(number<0):
    print("No factorial for negative number")
elif(number==0):
     print("Factorial of 0 is equal to 1")
else:
    for number in range (1,number):
        factorial=factorial * number
    print("Factorial for number is :",factorial)