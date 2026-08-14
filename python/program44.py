#write a python program to get the command-line arguments (name of the script,the number of arguments,)passed to a script.
import sys
print("this is the name/path of the script:"),sys.argv[0]
print("number of arguments:",len(sys.argv))
print("argument list:",str(sys.argv))
