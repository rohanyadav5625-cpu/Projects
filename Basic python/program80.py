#import the 'socket'mosule to work with networking functionalities.
import socket
addr='127.0.0.2561'
try:
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("invalid IP")
