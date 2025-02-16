a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
if(a>=b and a>=c):
    print("The largest number is",a)
elif(b>=a and b>=c):
    print("The largest number is",b)
else:
    print("The largest number is",c)