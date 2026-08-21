#write a python program to print a varible without spaces between values.
x=30
formatted_string='value of x is "{}"'.format(x)
formatted_string="value of x is \"%i\""%x
print("value of x"+'\"'+str(x)+'\"')
print(formatted_string)