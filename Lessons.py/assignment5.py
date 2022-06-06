#Geometric Progression
a=int(input("Enter the first term "))
r=int(input("Enter common ratio "))
n=int(input("Enter number of terms "))

for i in range (1, n+1):
    n_term=a*r*(i-1)
    print(n_term)

