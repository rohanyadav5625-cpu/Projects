#import  the 'title'module to work time-related function 
import time
def sum_of_n_number (n):
    start_time=time.time()
    s=0
    for i in range(1,n+1):
        s=s+1
    end_time=time.time()
    return s,end_time- start_time
n=5
print("\ntime to sum of 1 to",n,"and required time to calculate is :",sum_of_n_number(n))