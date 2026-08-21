#write a python program to find files and skip directiries in a given directory.
import os
print([f for f in os.listdir('/home/student')if os.path.isfile(os.path.join('/home/student',f))])