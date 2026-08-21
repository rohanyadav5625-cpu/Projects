#prompt the user to input a number of days and store it in the varible 'days'.
days=int(input("input days:"))*3600*24
hours=int(input("input hours:"))*3600
minutes=int(input("input minutes:"))*60
seconds=int(input("input seconds:"))
time=days+hours+minutes+seconds
print("the amount of seconds:",time)