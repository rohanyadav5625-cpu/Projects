#import the 'os' module to work with the operating system.
import os
user_path='d:/'
for fname in os.listdir(user_path):
    path=os.path.join(user_path,fname)
    if os.path.isdir(path):
     continue
    print(fname)
