#find the factorial of a number
num=int(input("enter the number"))
fact=1
if(num<0):
    print(" Not able to find the factorial of a negative number")
elif(num==0):
    print("the factorial of a 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("the factorial of a number is",fact)
