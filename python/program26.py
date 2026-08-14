#import the 'socket ' module to work with network-related functions.
import socket
local_hostname = socket.gethostname()
ip_addresses=socket.gethostbyname_ex(local_hostname)[2]
filterd_ips=[ip for ip in ip_addresses if not ip.startswith("127.")]
first_ip=filterd_ips[:1]
print(first_ip[0])