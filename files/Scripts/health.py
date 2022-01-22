import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 7778
MESSAGE = b"\\info\\"
sock = socket.socket(socket.AF_INET, # Internet
                       socket.SOCK_DGRAM) # UDP
sock.setblocking(True)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
if data is not None:
    sock.close()
    exit(0)
else:
    exit(1)