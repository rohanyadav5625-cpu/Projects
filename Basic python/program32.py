#import the sqrt function from the math module to calculate the square root.
from math import sqrt
print("input lenghs of shorter traingle sides:")
a=float(input("a:"))
b=float(input("b:"))
c=sqrt(a**2+b**2)
print("the length of the hypotenuse is:",c)
