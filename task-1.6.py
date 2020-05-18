#task-1.6
#Program to create simple calculator in Python which on input of 1,2,3,4 should add , subtract , multiply and divide respectively.
n=int(input("Enter 1st Number="))#stores the 1st number
m=int(input("Enter 2nd Number="))#stores the second number
u=int(input("Enter 1 for addition ,2 for Subtraction,3 for multiplication & 4 for division="))#stores the option that u want to operate on both
if(u==1):#if uequals to 1 then it adds n and m
    print(f"Addition of {n} and {m} = {n+m}")#adds two number
elif(u==2):#if u equals to 2 then it subtract m from n
    print(f"Subtraction of {n} and {m} = {n-m}")#subtract two number
elif(u==3):#if u eaquals to3 then it multiply n by m
    print(f"Multiplication of {n} and {m} ={n*m}")#multiply two number
elif(u==4):#if u eqauls to 4 then it divides n by m
    print(f"Division of {n} and {m} = {n/m}")#divide two number
      
