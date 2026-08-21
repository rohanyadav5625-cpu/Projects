#import the the 'sys' module, which provides access to some varibles used or maintained by the interpreter 
import sys
def eprint (*args,**kwargs):
   print(*args,file=sys.stderr,**kwargs)
eprint ("abc","efg","xyz",sep="--")
