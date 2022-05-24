

age=input ("What is your age?")
acc_bal=0
acc_bal= acc_bal + 10000

if (int(age))>25 and (int(age))<30 :
    print ("Confirmed you have received ksh.10000")
    
else:
 print ("Sorry no money for you")


#Write a program to withdraw ksh.25000 if the acc bal
#is between 100000-200000
#30% if the acc bal is btwn 500000-1000000
#Above 1M deduct 15000


acc_bal=input ("What is your acc_bal?")
if (int(acc_bal))>100000 and (int(acc_bal))<200000 :
    acc_bal=acc_bal-25000
    print ("We have deducted ksh.25000")

elif(int(acc_bal))>500000 and (int(acc_bal))<1000000 :
    acc_bal =acc_bal-(acc_bal*0.3)
    print ("We have deducted 30000")

elif (int(acc_bal))>1000000 :
 acc_bal= acc_bal-15000 
 print("We have deducted ksh.15000")
else:
    print("No deduction")



