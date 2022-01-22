import socket
# Checks the health of the UT server by running the 'info' query against it.
# If the server responds then we exit code 1, docker assumes the server is healthy.
# Relies on the Docker HEALTHCHECK for timeout, retires and error handling. 

UDP_IP = "127.0.0.1"
UDP_PORT = 7778
MESSAGE = b"\\info\\"
sock = socket.socket(socket.AF_INET, # Internet
                       socket.SOCK_DGRAM) # UDP
sock.setblocking(True)
# Send info query to server
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

# Wait for response
data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
if data is not None:
    sock.close()
    exit(0)
else:
    exit(1)
