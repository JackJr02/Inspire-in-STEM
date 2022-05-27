a=int (input("Enter the first number"))
d=int (input("Enter number"))
n=int (input("Enter number"))

for i in range (a,n+1):
  n_terms= a+d *(i-1)
print (n_terms)
s_n= n/2* (2*a+(n+1)*d)
print (s_n)