#finding the given triangle iscosceles,scalar or equilateral
s1=int(input("enter the first side of triangle"))
s2=int(input("enter the second side of triangle"))
s3=int(input("enter the third side of triangle"))
if(s1==s2 and s1==s3):
    print("The triangle is equilateral")
elif(s1==s2 and s1!=s2)or(s2==s3 and s2!=s1)or(s3==s1 and s3!=s1):
    print("The triangle is isosclance")
else:
    print("The tiangle is scalar")