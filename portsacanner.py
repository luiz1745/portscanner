import socket
LHOST="192.168.56.1"
for PORTS in range(1, 6535) :
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result=s.connect_ex((LHOST, PORTS))
    if result ==0:
        print("{} open/aberta".format(PORTS))
    else:
        pass