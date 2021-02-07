'''
Programming and Language Version: Python3 3.8.6
Testing Environment: 
    OS: Ubuntu 20.10 x86_64
    Command Lines: 
        1. To simulate a running connection: 
            a. Compile dnsclient.py using python3 dnsclient.py 127.0.0.1 9999 host1.student.test
            b. Compile dnsserver.py using python3 dnsserver.py 127.0.0.1 9999
'''

import sys
import socket

serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

# Create a UDP socket. Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Assign server IP address and port number to socket
serverSocket.bind((serverIP, serverPort))

file = open("dns-master.txt", "r")
test = False
print("The server is ready to receive on port:  " + str(serverPort) + "\n")

while True:
    sendLine = " "
    line = " "
    data, address = serverSocket.recvfrom(1024)
    
    values = data.decode()
    message = values.rstrip().split()
    
    for line in file:
        li=line.strip()
        if not li.startswith("#"):
            words = line.rstrip().split()
            if words:
                if words[0] == message[0]:
                    sendLine = line
                    test = True
                    break
           
    if test:
        returnMessage = "0" + " " + sendLine
        serverSocket.sendto(returnMessage.encode(),address)
    else:
        returnMessage = "1"
        serverSocket.sendto(returnMessage.encode(),address)
