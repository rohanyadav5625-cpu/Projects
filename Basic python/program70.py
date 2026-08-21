#define a function that checks if all varibles passed as arguments have the same value.
def multiple_varibles_equality(*vars):
    for x in vars:
        if x !=vars[0]:
          return "all varibles do not have the same value."
        return "all varibles have the same value."
print(multiple_varibles_equality (2,3,2,2,2,2))
print(multiple_varibles_equality(10,10,10,10))
print(multiple_varibles_equality(-3,-3,-3,-3))