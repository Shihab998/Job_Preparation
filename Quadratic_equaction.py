import math

a = int(input("Enter the vale of x**2: "))
b = int(input("Enter  the vale of x: "))
c = int(input("Enter the vale of constant: "))

if b**2 - (4*a*c) > 0:

    x1= (-b + math.sqrt(b**2-4*a*c)) / 2*a

    x2=(-b - math.sqrt(b**2-4*a*c)) / 2*a

    print("The value of x are",x1, x2)
else:
   print("Unable to find value of x")


 

