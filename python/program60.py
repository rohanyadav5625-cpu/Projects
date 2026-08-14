#import the 'reduce'fuction from the 'functools'module.
from functools import reduce
nums=[10,20,30]
print("orignal list number:")
print(nums)
nums_product =reduce((lambda x,y:x*y),nums)
print("\nproduct of the said numbers(without using a for loop):",nums_product)
