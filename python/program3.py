#import the 'date'class from the 'datetime'module
from datetime import date
#define a start date as july 2,2014 
f_date = date (2014,7,2)
#define an end date as july 11,2014 
i_date = date (2014,7,11)
#calculate the difference between the end date and start date 
delta=i_date -f_date
#print the number of days in the time difference 
print(delta.days)
#define the value of pi 
pi=3.1415926535897931
#define the radius of the sphere 
r=6.0
#calculate the volume of the sphere using the formula 
v=4.0/3.0*pi*r**3
#print the calculate volume of the sphere 
print ('the volume of the sphere is:',v)