'''
Programming and Language Version: Python3 3.8.6
Testing Environment: 
    OS: Ubuntu 20.10 x86_64
    Command Lines: 
        1. To simulate a running connection: 
            a. Compile server.py using python3 server.py 127.0.0.1 12000
            b. Compile client.py using python3 server.py 127.0.0.1 12000
'''
import sys
import socket
import random
import struct

# Read server IP address and port from command-line arguments
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

# Create a UDP socket. Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Assign server IP address and port number to socket
serverSocket.bind((serverIP, serverPort))

print("The server is ready to receive on port:  " + str(serverPort) + "\n")

# loop forever listening for incoming UDP messages
while True:
    # Receive and print the client data from "data" socket
    data, address = serverSocket.recvfrom(1024)

    # Echo back to client
    randNum = random.randint(0,10)
    if randNum >= 4:
        print("Responding to ping request with sequence number " 
                                    + str(struct.unpack('i', data)).strip("(,)"))
        serverSocket.sendto(data,address)
    else:
        print("Message with sequence number " 
                    + str(struct.unpack('i', data)).strip("(,)") + " dropped")
    
