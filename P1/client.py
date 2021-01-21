'''
Programming and Language Version: Python3 3.8.6
Testing Environment: 
    OS: Ubuntu 20.10 x86_64
    Command Lines: 
        1. To simulate a running connection: 
            a. Compile server.py using python3 server.py 127.0.0.1 12000
            b. Compile client.py using python3 server.py 127.0.0.1 12000
        2. To simulate a connection error:
            a. Compile client.py using python3 server.py 127.0.0.1 12000
'''
#! /usr/bin/env python3
# Echo Client
import sys
import socket

# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
count = int(sys.argv[3])
data = 'X' * count # Initialize data to be sent

# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Default socket timeout
clientsocket.settimeout(1)

# Receive the server response and send data to server
for i in range(3):
    try: 
        print("Sending data to   " + host + ", " + str(port) + ": " + data + " (" + str(count) + " characters)")
        clientsocket.sendto(data.encode(),(host, port))
        dataEcho, address = clientsocket.recvfrom(count)
        print("Receive data from " + address[0] + ", " + str(address[1]) + ": " + dataEcho.decode())
        break
    except:
        print("Message timed out")
    
#Close the client socket
clientsocket.close()
