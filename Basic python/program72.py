#define a fuction 'lower_case_str'that takes a text as input.
def lower_case_str(text):
    ctr=0
    for char in text:
        if (ord(char)>=97 and ord(char)<=122):
            ctr=ctr+1
            if(ctr>0):
                return True
str1='A8238i823acdeOUEI'
print("orignal string:",str1)
print("Lowercase letters exist in the said string:",lower_case_str(str1))
str1='PYTHON'
print("\nOrignal string:",str1)
print("Lowercase letters exist in the said string:",lower_case_str(str1))
str1='javascript'
print("\nOrignal string:",str1)
print("Lowercase letters exist in the said string:",lower_case_str(str1))
