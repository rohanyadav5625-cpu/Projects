#import 'os' module for interacting with the operating system.
import os 
print("current dir:",os.getcwd())
os.chdir('c:')
file_list=filter(os.path.isfile,os.listdir('.'))
sorted_file=sorted(file_list,key=os.path.getmtime)
print('\n'.join(map(str,sorted_file)))