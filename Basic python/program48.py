#define a function 'dict_sum'that takes a dictionary 'nums'as input and calculate the sum of its values.
def dict_sum(nums):
    num_sum=0
    for i in nums:
        num_sum=num_sum+nums[i]
    return num_sum
nums={'a':100,'b':200,'c':300,'d':120}
print("orignal container:")
print(nums)
print(type(nums))
print("sum of all items of the said container:",dict_sum(nums)) 