#define a function 'test' that takes a list 'nums' and an integer 'n' as argument.
def test(nums,n):
    return (all(x>n for x in nums))
nums=[10,20.30,40,50,60,70,80,90,100]
print("orignal list numbers:")
print(nums)
n=12
print("\ncheck whether all number of the said list are greater than",n)
print(test(nums,n))
n=5
print("\ncheck whether all numbers of the said list are grater than",n)
print(test(nums,n))
