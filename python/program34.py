#import the 'os.path'and 'time' modules to work with file system paths and timestamps.
import os,time
filename="program33.py"
if os.path.exists(filename):
  print("Last modified: %s" % time.ctime(os.path.getmtime("filename")))
  print("Created: %s" % time.ctime(os.path.getctime("filename")))
else:
  print("rohan yadav -",filename)
