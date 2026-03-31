import math
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
d=(a*a)-4*a*c
if(d>0):
    print("Root Exist")
    r1=(b*math.sqrt(d))/2*a
    r2=-(b*math.sqrt(d))/2*a
    print("roots are ",r1,r2)
    
elif(d==0):
    print("roots exist")
    r1=b/(2*a)
    r2=-b/(2*a)
    print("roots are",r1,r2)
else:
    print("imaginary roots")
    
