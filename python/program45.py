#import the sys module to use sys.getsizeof()
import sys
str1="one"
str2="four"
str3="three"
x=0
y=112
z=122.56
print("size of",str1,"=",str(sys.getsizeof(str1))+"bytes")
print("size of",str2,"=",str(sys.getsizeof(str2))+"bytes")
print("size of",str3,"=",str(sys.getsizeof(str3))+"bytes")
print("size of",x,"=",str(sys.getsizeof(x))+"bytes")
print("size of",y,"=",str(sys.getsizeof(y))+"bytes")
L=[1,2,3,'red','black']
print("Size of",L,"=",sys.getsizeof(L),"bytes")
T=("red",[8,4,6],(1,2,3))
print("size of",T,"=",sys.getsizeof(T),"bytes")
S={'apple','orange','apple','pear'}
print("size of",S,"=sys.getsizeof(S),bytes")
D={'name':'david','age':6,'class':'first'}
print("size of",D,"=",sys.getsizeof(S),"bytes")    