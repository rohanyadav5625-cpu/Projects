#define a function named "tail"that takes a "list" as input.
def tail(lst):
    if len (lst)>1:
        return lst[1:]
    else:
        return lst
print(tail([1,2,3,4]))
print(tail([1]))
print(tail(["red","black","green","white","orange"]))
