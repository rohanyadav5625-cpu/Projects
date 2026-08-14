#create an infinite loop using "while True".
while True:
    try:
        a=int(input("input a number :"))
        break 
    except ValueError:
     print("\nthis is not a number.Try again...")
     print()
