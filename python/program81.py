#import the 're'module to work with regular expressions.
import re
ip_regrex="^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
def check_ip_address(user_ip):
    if re.search(ip_regrex,user_ip):
      return"valid IP address"
    else:
      return"invalid IP address"
user_ip="10.0.0.0"
print("\n",user_ip,"->",check_ip_address(user_ip))
user_ip="10.255.255.255"
print("\n",user_ip,"->",check_ip_address(user_ip))
user_ip="192.168.255.0"
print("\n",user_ip,"->",check_ip_address(user_ip))
user_ip="266.1.0.2"
print("\n",user_ip,"->",check_ip_address(user_ip))
user_ip="01.102.103.104"
print("\n",user_ip,"->",check_ip_address(user_ip))







