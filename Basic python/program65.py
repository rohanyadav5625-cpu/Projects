#write a python program to determine if a varible is defined or not.
try:
    x=1
except NameError:
    print("varible is not defined....!")
else:
    print("varible is defined.")
    try:
        y
    except NameError:
        print("varible is not defined....!")
    else:
        print("varible is defined:")
